<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { pageName } from '../../stores/admin.js';

	let data

	onMount(async () => {
		pageName.update(() => document.title);

		try {
			const response = await fetch('http://localhost:8080/auth/user', {
				headers: {'Content-Type': 'application/json'},
				credentials: 'include',
			})
			const content = await response.json()
			data = content

			if (response.status == 401) {
				goto('/')
			} else {
				console.log(content)
			}
		} catch (error) {
			goto('/')
		}
	});
	console.log(data)
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>

<!-- Cards -->
<div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-3">
	<!-- Total questionnaire card -->
	<div
		class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
	>
		<div
			class="p-3 mr-4 text-orange-500 bg-orange-100 rounded-full dark:text-orange-100 dark:bg-orange-500"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5"
				viewBox="0 0 20 20"
				fill="currentColor"
			>
				<path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
				<path
					fill-rule="evenodd"
					d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
					clip-rule="evenodd"
				/>
			</svg>
		</div>
		<div>
			<p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Monitoring Form</p>
			<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">5</p>
		</div>
	</div>

	<!-- Subscribers card -->
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
			<p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Pasien Monitoring</p>
			<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">48</p>
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
			<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">376</p>
		</div>
	</div>
</div>

<!-- Table -->
<div class="w-full overflow-hidden rounded-lg shadow-xs">
	<div class="w-full overflow-x-auto">
		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Resnpon Terbaru</th>
					<th class="px-4 py-3">Form Monitoring</th>
					<th class="px-4 py-3">Tanggal</th>
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							<!-- Avatar with inset shadow -->
							<!-- <div class="relative hidden w-8 h-8 mr-3 rounded-full md:block">
								<img
									class="object-cover w-full h-full rounded-full"
									src="https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjE3Nzg0fQ"
									alt=""
									loading="lazy"
								/>
								<div class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true" />
							</div> -->
							<div>
								<p class="font-semibold">Hans Burger</p>
							</div>
						</div>
					</td>
					<td class="px-4 py-5 text-sm"> jj-psoriasis </td>

					<td class="px-4 py-5 text-sm"> 6/10/2020 </td>
				</tr>
			</tbody>
		</table>
	</div>
</div>
