<script>
    export let title, message
</script>
<div class="w-full overflow-hidden rounded-lg shadow-x min-h-max mt-40">
    <div class="w-full overflow-x-auto flex flex-col justify-center items-center text-center">
        <div class="mb-20">
            <h5 class="font-bold text-2xl mb-3 text-neutral-600">{ title }</h5>
            <p class="text-sm italic text-neutral-500 max-w-lg">{ message }</p>
        </div>
        
        <img src="/img/empty500.png" alt="No entries" class="w-max">
    </div>
</div>