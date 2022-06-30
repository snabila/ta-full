<script>
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../stores/admin.js';

	onMount(() => {
		pageName.update(() => document.title);
	});

</script>

<svelte:head>
	<title>John Doe</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	<!-- Details -->
	<div>
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
		<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Nama</p>
				<p class="col-span-2 ml-2">Hans Burger</p>
			</div>
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Username</p>
				<p class="col-span-2 ml-2">hans_burger</p>
			</div>
			
		</div>
	</div>

	<!-- Forms -->
	<div>
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Monitoring Psoriasis</h4>
		<!-- Numerik : chart -->
		<!-- <div class="grid gap-6 mb-8 md:grid-cols-2">
			<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
				<h5 class="font-semibold text-gray-600 dark:text-gray-300">Kualitas Tidur</h5>
				<div class="chart-container">
					<LayerCake
						ssr={true}
						percentRange={true}
						padding={{ top: 20, right: 10, bottom: 20, left: 25 }}
						x="x"
						y="y"
						yDomain={[0, null]}
						data={points}
					>
						<Html>
							<!-- <Labels /> -->
							<!-- <AxisX formatTick={formatDate} />
							<AxisY />
						</Html>
						<ScaledSvg>
							<Line />
						</ScaledSvg>
					</LayerCake>
				</div>
			</div>
		</div> -->

		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Tanggal</th>
					<th class="px-4 py-3">Stress</th>
					<th class="px-4 py-3">Tidur</th>
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5 text-sm"> 6/10/2020 </td>
					<td class="px-4 py-5 text-sm">10</td>
					<td class="px-4 py-5 text-sm">1</td>
				</tr>
			</tbody>
		</table>
	</div>
</div>

<style>
	/*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will
    expand to fill it.
  */
	.chart-container {
		width: 100%;
		height: 300px;
		padding-top: 16px;
	}
</style>
