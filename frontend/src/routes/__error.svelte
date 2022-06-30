<script context="module">
    export function load({ error, status }) {
        return {
            props: {
                status: status,
                message: error.message
                // title: `${status}: ${error.message}`
            }
        };
    }
</script>

<script>
    export let status, message;
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>

<main class="h-screen max-h-screen bg-gray-50">
    <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full text-center">
            <h1 class="mb-4 text-9xl font-extrabold text-gray-300">{status}</h1>
            <p class="mb-6">{message}</p>
            <a href="/" class="text-violet-600 text-sm">Kembali</a>
        </div>
    </div>
</main>