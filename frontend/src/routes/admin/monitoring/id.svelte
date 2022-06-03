<script>
	import { onMount } from 'svelte';

	import { pageName } from '../stores';

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<svelte:head>
	<title>Monitoring Psoriasis</title>
</svelte:head>

<!-- Cards -->
<div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-2">
	<!-- Total questionnaire card -->
	<div
		class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
	>
		<div
			class="p-3 mr-4 text-green-500 bg-green-100 rounded-full dark:text-green-100 dark:bg-green-500"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5"
				viewBox="0 0 20 20"
				fill="currentColor"
			>
				<path
					d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"
				/>
			</svg>
		</div>
		<div>
			<p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Jumlah Pasien</p>
			<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">7</p>
		</div>
	</div>

	<!-- Responds card -->
	<div
		class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
	>
		<div
			class="p-3 mr-4 text-blue-500 bg-blue-100 rounded-full dark:text-blue-100 dark:bg-blue-500"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5"
				viewBox="0 0 20 20"
				fill="currentColor"
			>
				<path
					fill-rule="evenodd"
					d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z"
					clip-rule="evenodd"
				/>
			</svg>
		</div>
		<div>
			<p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Total Respon</p>
			<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">27</p>
		</div>
	</div>
</div>
