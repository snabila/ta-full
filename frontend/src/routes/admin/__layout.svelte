<script>
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { ScaleOut } from 'svelte-loading-spinners'
	import Sidebar from '../../components/admin/sidebar.svelte';
	import Header from '../../components/admin/header.svelte';

	let spinner
    onMount(() => {
		setTimeout(() => {
			spinner = true;
		}, 2000);
	});
</script>

{#if !spinner}
<div class="absolute z-50 w-screen h-screen bg-gray-50 flex items-center justify-center" in:fade out:fade>
	<ScaleOut size="60" color="#9333ea" unit="px" duration="1s"></ScaleOut>
</div>
{/if}

<div class="flex h-screen bg-gray-50 dark:bg-gray-900">
	<Sidebar />
	<div class="flex flex-col flex-1 w-full">
		<Header />
		<main class="h-full overflow-y-auto">
			<div class="container px-6 mx-auto grid" >
				<slot />
			</div>	
		</main>
	</div>
</div>
