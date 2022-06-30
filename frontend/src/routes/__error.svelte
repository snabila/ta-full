<script context="module">
    export function load({ error, status }) {
        return {
            props: {
                status: status,
                message: error.message
                // title: `${status}: ${error.message}`
            }
        };
    }
</script>

<script>
    import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { ScaleOut } from 'svelte-loading-spinners'
    export let status, message;

    let spinner
    onMount(() => {
		setTimeout(() => {
			spinner = true;
		}, 2000);
	});
</script>

<svelte:head>
	<title>{status}</title>
</svelte:head>

{#if !spinner}
<div class="absolute z-20 w-screen h-screen bg-gray-50 flex items-center justify-center" in:fade out:fade>
	<ScaleOut size="60" color="#9333ea" unit="px" duration="1s"></ScaleOut>
</div>
{/if}

<main class="h-screen max-h-screen bg-gray-50" out:fade>
    <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full text-center">
            <h1 class="mb-4 text-9xl font-extrabold text-gray-300">{status}</h1>
            <p class="mb-6">{message}</p>
            <a href="/" class="text-violet-600 text-sm">Kembali</a>
        </div>
    </div>
</main>