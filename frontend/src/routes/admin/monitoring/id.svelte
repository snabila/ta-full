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
<div class="grid gap-6 mb-8 md:grid-cols-2">
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

<!-- First section : details & settings -->
<div class="grid gap-6 mb-8 md:grid-cols-3 xl:grid-cols-3">
	<!-- Left -->
	<div class="md:col-span-2">
		<!-- Details -->
		<div>
			<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
			<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
				<div class="grid grid-cols-3 mb-4">
					<p class="font-semibold">Nama Form</p>
					<p class="col-span-2 ml-2">Monitoring Psoriasis</p>
				</div>
				<div class="grid grid-cols-3 mb-4">
					<p class="font-semibold">Kode Form</p>
					<p class="col-span-2 ml-2">username-psoriasis</p>
				</div>
				<div class="grid grid-cols-3">
					<p class="font-semibold">Deskripsi</p>
					<p class="col-span-2 ml-2 leading-relaxed">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non lacus vestibulum,
						consequat metus at, efficitur nulla. Aliquam vitae diam pretium, tempor diam et, porta
						ante. Proin eu lacus lectus.
					</p>
				</div>
			</div>
		</div>

		<!-- Fields -->
		<div>
			<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Fields</h4>
			<div class="px-5 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm divide-y">
				<div class="py-4">
					<p class="font-semibold italic mb-4">Field 1</p>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Label</p>
						<p class="col-span-2 ml-2">Kualitas Tidur</p>
					</div>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Tipe Jawaban</p>
						<p class="col-span-2 ml-2">Numerik</p>
					</div>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Pertanyaan</p>
						<p class="col-span-2 ml-2">Berapa lama kamu tidur tadi malam?</p>
					</div>
				</div>
				<div class="py-4">
					<p class="font-semibold italic mb-4">Field 2</p>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Label</p>
						<p class="col-span-2 ml-2">Stress Level</p>
					</div>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Tipe Jawaban</p>
						<p class="col-span-2 ml-2">Numerik</p>
					</div>
					<div class="grid grid-cols-3 mb-4">
						<p class="font-semibold">Pertanyaan</p>
						<p class="col-span-2 ml-2">Berapa lama kamu tidur tadi malam?</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Right -->
	<div>
		<!-- Pengaturan -->
		<div>
			<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pengaturan</h4>
			<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
				<div class="flex justify-between mb-4">
					<p class="font-semibold">Reminder</p>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 text-green-500"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>

				<div class="flex justify-between mb-6">
					<p class="font-semibold">Open join</p>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 text-red-600"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>

				<a
					class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple mb-4"
					href="#"
				>
					Edit Form
				</a>

				<a
					class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-red-600 transition-colors duration-150 bg-white border border-red-600 rounded-lg active:bg-red-100 hover:bg-red-100 focus:outline-none focus:shadow-outline-purple"
					href="#"
				>
					Hapus Form
				</a>
			</div>
		</div>

		<!-- Pasien -->
		<div>
			<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pasien</h4>
			<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
				<!-- Header -->
				<div class="flex justify-between mb-4">
					<p class="font-semibold">Total</p>
					<p class="font-semibold">24</p>
				</div>

				<hr />

				<!-- List pasien -->
				<div class="flex justify-between items-center mt-4">
					<div class="flex items-center text-sm">
						<!-- Avatar with inset shadow -->
						<div class="relative hidden w-8 h-8 mr-3 rounded-full xl:block">
							<img
								class="object-cover w-full h-full rounded-full"
								src="https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjE3Nzg0fQ"
								alt=""
								loading="lazy"
							/>
							<div class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true" />
						</div>
						<div>
							<p class="font-semibold">Hans Burger</p>
						</div>
					</div>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-4 w-4 ml-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="2"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
						/>
					</svg>
				</div>

				<button class="mt-6 flex items-center justify-center w-full text-purple-600">
					View All
					<span>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5 ml-2"
							viewBox="0 0 20 20"
							fill="currentColor"
						>
							<path
								fill-rule="evenodd"
								d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
								clip-rule="evenodd"
							/>
						</svg>
					</span>
				</button>
			</div>
		</div>
	</div>
</div>
