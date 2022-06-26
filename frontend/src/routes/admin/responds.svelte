<script>
	import { onMount } from 'svelte';

	import { pageName } from '../../stores/admin';

	// // onMount(async () => {
	// // 	pageName.update(() => 'Dashboard');
	// // });

	// // let displayPageName;

	// // pageName.subscribe((value) => {
	// // 	displayPageName = value;
	// // });

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<svelte:head>
	<title>Respon</title>
</svelte:head>

<!-- Table -->
<div class="w-full overflow-hidden rounded-lg shadow-xs">
	<div class="w-full overflow-x-auto">
		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Respon Terbaru</th>
					<th class="px-4 py-3">Form Monitoring</th>
					<th class="px-4 py-3">Tanggal</th>
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							
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