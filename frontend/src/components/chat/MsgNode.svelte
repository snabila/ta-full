<script>
    import { fade } from 'svelte/transition';
	export let objAttributes = {};
</script>

<div class="inline-flex mb-5 w-full">
    {#if objAttributes.type == 'bot'}
        <div class="mr-5">
            <div class="first:opacity-100 h-10 w-10 bg-slate-900 " />
        </div>
        <div class="bg-white py-4 px-6 border-0 rounded-md drop-shadow-md">
            <p class="whitespace-pre-line">{objAttributes.msg}</p>
        </div>
    {:else}
        <div class="bg-violet-700 text-white py-4 px-6 border-0 rounded-md max-w-sm drop-shadow-md ml-auto">
            <p class="whitespace-pre-line">{objAttributes.msg}</p>
        </div>
    {/if}  
</div>