<script>
	import { goto } from '$app/navigation';
	import { fade, fly } from 'svelte/transition';
	import { messageStore } from '../stores/chat'
	import MsgList from '../components/chat/MsgList.svelte'

	export let auth, authUser

	let message = ''
	let messageField

	const submit = async () => {
		// tambahin pesan user ke array buat tampilin di ui
		const newMessage = {
			'id': String($messageStore.length),
			'type': 'user',
			'msg': message
		}

		messageStore.update((currentMessage) => {
			return [newMessage, ...currentMessage]
		})

		// panggil api chatbot buat dapetin respons
		const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
			body: JSON.stringify({
                'sender' : authUser.username,
				'message' : message
            })
		})
		const content = await response.json()

		// tambahin respons bot ke array buat tampilin di ui
		content.forEach(element => {
			let newMessageBot = {
				'id': String($messageStore.length),
				'type': 'bot',
				'msg': element['text']
			}

			messageStore.update((currentMessage) => {
				return [newMessageBot, ...currentMessage]
			})
		});

		console.log(content[0]['text'])

		// reset input field
		messageField.value = ''
		console.log($messageStore)
    }

	const logout = async () => {
		await fetch('http://localhost:8080/auth/logout', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		auth = false
		await goto('/login')
	}
</script>

<script context="module">
	export async function load({ fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})

		let data = await response.json()
		// console.log(response.status)
		
		if (response.status == 200) {
			return {
				props: {
					auth: true,
					authUser: data
				}
			}
		} else {
			return {
				props: { auth: false, authUser: [] }
			}	
		}
	}	
</script>

<svelte:head>
	<title>Healthcare Chatbot</title>
</svelte:head>

<div class="bg-gray-50 max-h-screen h-screen w-screen overflow-y-scroll">
	<div class="max-w-2xl mx-auto">
		<header class="mx-auto px-3 max-w-2xl flex items-center justify-between">
			{#if auth}
				<h1 class="text-xl my-8 w-max inline-block">Halo {authUser.name}!</h1>
			{:else}
				<h1 class="text-xl my-8 w-max inline-block">Halo!</h1>
			{/if}
			<div class="w-max inline-block">
				{#if auth}
					{#if authUser.role == 'dokter'}<a href="/admin" class="text-purple-600">Admin</a>{/if}
					<button on:click={logout} class="ml-2 text-purple-600">Logout</button>
				{:else}
					<a href="/login" class="text-purple-600">Login</a>
					<a href="/signup" class="ml-2 text-purple-600">Register</a>
				{/if}
			</div>
		</header>
		<main class="mx-auto px-3 max-w-2xl flex flex-col flex-grow">
			<div class="mb-6">
				<div class="inline-flex w-full mb-3">
					<form on:submit|preventDefault={submit} class="inline-flex w-full mb-3">
						{#if !auth}
						<input
							class="px-3 py-3 rounded-md w-full bg-gray-100 transition focus-visible:outline-none border-2 border-gray-200"
							type="text"
							name="pesan"
							id="pesan"
							placeholder="Harap login terlebih dahulu"
							disabled
						/>
						<button
							class="bg-violet-700 text-white px-4 rounded-md ml-3 transition" disabled
							>Send</button
						>

						{:else}
						<input
							class="px-3 py-3 rounded-md w-full bg-white focus:ring-violet-100 focus:ring-4 transition focus-visible:outline-none border-2 border-purple-600"
							type="text"
							name="pesan"
							id="pesan"
							placeholder="Ketik pesan"
							bind:value={message}
							bind:this={messageField}
						/>
						<button
							class="bg-violet-700 text-white px-4 rounded-md ml-3 hover:drop-shadow hover:bg-violet-500 transition "
							>Send</button
						>
						{/if}
					</form>
				</div>
				<div class="rounded-md bg-violet-100 px-1 py-2 text-center text-sm text-violet-500">
					<p>Ketikkan <code>`fungsi`</code> untuk melihat daftar fungsi chatbot</p>
				</div>
			</div>
			<MsgList />
		</main>
	</div>
</div>