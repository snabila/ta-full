<script>
	import { fade } from 'svelte/transition';
	import { storeFields } from '../../routes/admin/stores.js';
	export let objAttributes = {};
	//export let store;

	// function updateID(item) {
	// 	let updatedID = 1;
	// 	item.array.forEach((element) => {
	// 		element.id = updatedID;
	// 		updatedID++;
	// 	});
	// }

	function removeComponent() {
		// $storeFields = $storeFields.filter(function (value, index, arr) {
		// 	if (value.id != objAttributes.id) return value;
		// });

		// $storeFields.update((currentFeedback) => {
		// 	return currentFeedback.filter((item) => item.id != itemID);
		// });

		$storeFields = $storeFields.filter((element) => element.id != objAttributes.id);

		let updatedID = 1;

		$storeFields.forEach((element) => {
			element.id = updatedID;
			updatedID++;
		});

		// updateID($storeFields);

		console.log($storeFields);
	}
</script>

<div
	id="field-{objAttributes.id}"
	class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800"
	transition:fade
>
	<!-- Field ID -->
	<div class="flex items-center justify-between mb-4 text-sm font-semibold">
		<p class="italic">Field {objAttributes.id}</p>
		<button class="text-red-600 hover:underline" on:click={removeComponent}>Delete</button>
	</div>

	<!-- Nama Field -->
	<div class="mb-7">
		<label class="block text-sm mb-3 font-semibold" for="field-{objAttributes.id}-name">
			Label
		</label>
		<input
			class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
			placeholder="Temperatur"
			type="text"
			id="field-{objAttributes.id}-name"
			bind:value={objAttributes.label}
		/>
	</div>

	<!-- Tipe jawaban -->
	<div class="mb-7">
		<label for="field-{objAttributes.id}-type" class="block text-sm mb-3 font-semibold"
			>Tipe Jawaban</label
		>
		<select
			id="field-{objAttributes.id}-type"
			class="block mt-1 text-sm border rounded-md bg-white dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-2"
			bind:value={objAttributes.type}
		>
			<option value="1">Teks pendek</option>
			<option value="2">Numerik</option>
			<option value="3">Yes/No</option>
		</select>
	</div>

	<!-- Pertanyaan -->
	<div>
		<label class="block text-sm mb-3 font-semibold" for="field-{objAttributes.id}-quest">
			Pertanyaan
		</label>
		<input
			class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
			placeholder="Berapa suhu anda hari ini?"
			type="text"
			id="field-{objAttributes.id}-quest"
			bind:value={objAttributes.quest}
		/>
	</div>
</div>
