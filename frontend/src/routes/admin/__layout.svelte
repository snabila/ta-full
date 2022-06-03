<script>
	import Sidebar from '../../components/admin/sidebar.svelte';
	import Header from '../../components/admin/header.svelte';
</script>

<div class="flex h-screen bg-gray-50 dark:bg-gray-900">
	<Sidebar />
	<div class="flex flex-col flex-1 w-full">
		<Header />
		<main class="h-full overflow-y-auto">
			<div class="container px-6 mx-auto grid">
				<!-- Content slot -->
				<slot />
			</div>
		</main>
	</div>
</div>
