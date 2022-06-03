<script>
	import { onMount } from 'svelte';

	import { pageName } from '../stores';

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<svelte:head>
	<title>Form Monitoring</title>
</svelte:head>

<div class="w-full overflow-hidden rounded-lg shadow-xs">
	<div class="w-full overflow-x-auto">
		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Nama</th>
					<th class="px-4 py-3">Jumlah Pasien</th>
					<th class="px-4 py-3">Respon</th>
					<th class="px-4 py-3">Edit Terakhir</th>
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							<div>
								<a href="/admin/monitoring/id"><p class="font-semibold">Monitoring Psoriasis</p></a>
							</div>
						</div>
					</td>
					<td class="px-4 py-5 text-sm">12</td>
					<td class="px-4 py-5 text-sm">36</td>
					<td class="px-4 py-5 text-sm"> 6/10/2020 </td>
				</tr>
			</tbody>
		</table>
	</div>
</div>