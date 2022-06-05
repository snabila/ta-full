<script>
	import { onMount } from 'svelte';
	import { pageName } from '../stores.js';

	// chart stuffs
	import { LayerCake, ScaledSvg, Html } from 'layercake';
	import AxisX from '../../../components/layercake/AxisX.html.svelte';
	import AxisY from '../../../components/layercake/AxisY.html.svelte';
	import Line from '../../../components/layercake/Line.svelte';
	import Labels from '../../../components/layercake/Labels.html.svelte';
	import { timeParse, timeFormat } from 'd3-time-format';

	onMount(() => {
		pageName.update(() => document.title);
	});

	// chart trial
	const parseDate = timeParse('%Y-%m-%d');
	const formatDate = timeFormat('%B %d');

	const points = [
		{ x: parseDate('2022-06-05'), y: 5 },
		{ x: parseDate('2022-06-06'), y: 6 },
		{ x: parseDate('2022-06-07'), y: 5 },
		{ x: parseDate('2022-06-08'), y: 6 },
		{ x: parseDate('2022-06-09'), y: 5 },
		{ x: parseDate('2022-06-10'), y: 6 },
		{ x: parseDate('2022-06-11'), y: 5 },
		{ x: parseDate('2022-06-12'), y: 6 },
		{ x: parseDate('2022-06-13'), y: 5 }
	];
</script>

<svelte:head>
	<title>John Doe</title>
</svelte:head>

<!-- Details -->
<div>
	<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
	<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
		<div class="grid grid-cols-3 mb-4">
			<p class="font-semibold">Nama</p>
			<p class="col-span-2 ml-2">John Doe</p>
		</div>
		<div class="grid grid-cols-3 mb-4">
			<p class="font-semibold">Domisili</p>
			<p class="col-span-2 ml-2">Surabaya</p>
		</div>
		<div class="grid grid-cols-3 mb-4">
			<p class="font-semibold">Tanggal Lahir</p>
			<p class="col-span-2 ml-2">5 Juni 2022</p>
		</div>
		<div class="grid grid-cols-3">
			<p class="font-semibold">Gol. Darah</p>
			<p class="col-span-2 ml-2">A</p>
		</div>
	</div>
</div>

<!-- Forms -->
<div>
	<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Monitoring Psoriasis</h4>
	<!-- Numerik : chart -->
	<div class="grid gap-6 mb-8 md:grid-cols-2">
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
						<AxisX formatTick={formatDate} />
						<AxisY />
					</Html>
					<ScaledSvg>
						<Line />
					</ScaledSvg>
				</LayerCake>
			</div>
		</div>
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
