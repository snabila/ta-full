<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { fade } from 'svelte/transition';
    import { ScaleOut } from 'svelte-loading-spinners'
    
    let name = '', username = '', email = '', password = '', role = ''
    let error

    let spinner
    onMount(() => {
      setTimeout(() => {
        spinner = true;
      }, 2000);
    });

    const submit = async () => {
        const result = await fetch('http://localhost:8080/auth/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                username,
                email,
                password,
                role
            })
        })
        if (result.status == 200) {
          await goto('/login')
        } else {
          error = await result.json()
          console.log(error)
        }
    }
</script>

<script context="module">
	export async function load({ fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		
		if (response.status == 200) {
			return {
        status: 302,
        redirect: '/'
			}
		} else {
			return {}	
		}
	}	
</script>

<svelte:head>
	<title>Daftar</title>
</svelte:head>

{#if !spinner}
<div class="absolute z-20 w-screen h-screen bg-gray-50 flex items-center justify-center" in:fade out:fade>
	<ScaleOut size="60" color="#9333ea" unit="px" duration="1s"></ScaleOut>
</div>
{/if}

<main class="h-screen max-h-screen bg-gray-50" out:fade>
<div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Daftar akun baru</h2>
    </div>
    {#if error}
    <div class="rounded-md bg-red-100 px-1 py-2 text-center text-sm text-red-500">
      <p>{error.message}</p>
    </div>
    {/if}
    <form class="mt-8 space-y-6" on:submit|preventDefault={submit}>
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
          <div>
          <label for="nama" class="sr-only">Nama</label>
          <input bind:value={name} class="relative block w-full text-sm px-3 py-2 border rounded-md border-gray-200 placeholder-gray-500 text-gray-900 focus:ring-purple-500 focus:border-purple-500 focus:outline-none form-input focus:z-10" placeholder="Nama" required>
        </div>
        <div>
          <label for="username" class="sr-only">Username</label>
          <input bind:value={username} class="mt-4 relative block w-full text-sm px-3 py-2 border rounded-md border-gray-200 placeholder-gray-500 text-gray-900 focus:ring-purple-500 focus:border-purple-500 focus:outline-none form-input focus:z-10" placeholder="Username" type="text" required>
        </div>
        <div>
          <label for="email" class="sr-only">Email</label>
          <input bind:value={email} class="mt-4 relative block w-full text-sm px-3 py-2 border rounded-md border-gray-200 placeholder-gray-500 text-gray-900 focus:ring-purple-500 focus:border-purple-500 focus:outline-none form-input focus:z-10" placeholder="Email" type="email" required>
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input bind:value={password} class="mt-4 relative block w-full text-sm px-3 py-2 border rounded-md border-gray-200 placeholder-gray-500 text-gray-900 focus:ring-purple-500 focus:border-purple-500 focus:outline-none form-input focus:z-10" placeholder="Password" type="password" required>
        </div>
        <div>
          <label class="mt-4 text-sm block" for="role" >Daftar sebagai</label>
          <select
            id="role" bind:value={role}
            class="mt-2 block w-full text-sm border rounded-md bg-white dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-2"
		  >
            <option value="dokter">Dokter</option>
            <option value="pasien">Pasien</option>
          </select>
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500">
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <!-- Heroicon name: solid/lock-closed -->
            <svg class="h-5 w-5 text-purple-500 group-hover:text-purple-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
          </span>
          Daftar
        </button>
      </div>

      <div class="flex items-center justify-between">
        <div class="text-sm">
          <a href="/" class="font-medium text-purple-600 hover:text-purple-500"> Kembali </a>
        </div>
        <div class="text-sm">
          <a href="/login" class="font-medium text-purple-600 hover:text-purple-500"> Masuk </a>
        </div>
      </div> 
    </form>
  </div>
</div>
</main>