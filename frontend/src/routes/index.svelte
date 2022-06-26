<script>
	import { goto } from '$app/navigation';

	import {onMount} from 'svelte'
	import {authenticated, authrole} from '../stores/auth'
	// import {getCookie} from './../customfunctions'

	let name = ''
	let data

	let auth, role
	authenticated.subscribe(a => auth = a)
	authrole.subscribe(r => role = r)

	onMount(async () => {
		try {
			const response = await fetch('http://localhost:8080/auth/user', {
				headers: {'Content-Type': 'application/json'},
				credentials: 'include',
			})
			const content = await response.json()

			if (response.status == 401) {
				name = ''
				$authenticated = false
			} else {
				$authenticated = true
				$authrole = content.role
				
				console.log(role)
				data = content
				
				name = content.name
			}
		} catch (error) {
			name = ''
			$authenticated = false
		}
		
	})

	const logout = async () => {
		await fetch('http://localhost:8080/auth/logout', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		$authenticated = false
		name = ''
		await goto('/')
	}
</script>

<svelte:head>
	<title>Healthcare Chatbot</title>
</svelte:head>

<div class="bg-gray-50 max-h-screen h-screen overflow-y-hidden">
<header class="mx-auto px-3 max-w-2xl flex items-center justify-between">
	<h1 class="text-xl my-8 w-max inline-block">Halo {name}!</h1>
	<div class="w-max inline-block">
		{#if auth}
			{#if data.role == 'dokter'}<a href="/admin" class="text-purple-600">Admin</a>{/if}
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
			<input
				class="px-3 py-3 rounded-md w-full bg-white focus:ring-violet-100 focus:ring-4 transition focus-visible:outline-none"
				type="text"
				name="pesan"
				id="pesan"
				placeholder="Ketik pesan"
			/>
			<button
				class="bg-violet-700 text-white px-4 rounded-md ml-3 hover:drop-shadow hover:bg-violet-500 transition"
				>Send</button
			>
		</div>
	</div>

	<div class="overflow-y-scroll flex-grow">
		<!-- bot -->
		<div class="inline-flex mb-5 w-full">
			<div class="mr-5">
				<!-- avatar -->
				<div class="first:opacity-100 h-10 w-10 bg-slate-900 " />
			</div>
			<div class="bg-white py-4 px-6 border-0 rounded-md drop-shadow-md">
				<!-- content -->
				<p>
					Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem
					ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum
					lorem ipsum lorem ipsum
				</p>
			</div>
		</div>

		<!-- bot -->
		<div class="inline-flex mb-5 w-full">
			<div class="mr-5">
				<!-- avatar -->
				<div class="first:opacity-100 h-10 w-10 bg-slate-900 " />
			</div>
			<div class="bg-white py-4 px-6 border-0 rounded-md drop-shadow-md">
				<!-- content -->
				<p>
					Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem
					ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum
					lorem ipsum lorem ipsum
				</p>
			</div>
		</div>

		<!-- user -->
		<div class="inline-flex mb-5 w-full">
			<div
				class="bg-violet-700 text-white py-4 px-6 border-0 rounded-md max-w-sm drop-shadow-md ml-auto"
			>
				<!-- content -->
				<p>
					Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem
					ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum
					lorem ipsum lorem ipsum
				</p>
			</div>
		</div>
	</div>
</main>
</div>