<script>
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { ScaleOut } from 'svelte-loading-spinners'
	import Sidebar from '../../components/admin/sidebarAdmin.svelte';
	import Header from '../../components/admin/header.svelte';
	import {page} from '$app/stores'

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

<div class="flex h-screen bg-gray-50 dark:bg-gray-900" in:fade={{delay:500}} out:fade>
	<Sidebar />
	<div class="flex flex-col flex-1 w-full">
		<Header />
		<main class="h-full overflow-y-auto">
			<div class="container px-6 mx-auto grid pb-20" >
				<!-- {#key page}
				<div in:fade|local={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}> -->
				<slot />
				<!-- </div>
				{/key} -->
			</div>	
		</main>
	</div>
</div>