<script>
    import NoEntry from '../../../components/admin/NoEntry.svelte';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../stores/admin.js';
	import { parseDate } from '$lib/date.js'

    export let monitList
    // console.log(monitList)

    onMount(async () => {
		pageName.update(() => document.title);
	});
</script>

<script context="module">
    export async function load({ fetch }) {
        const response = await fetch('http://localhost:8080/auth/user', {
			method : 'GET',
			headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
			credentials: 'include',
		})

        let data = await response.json()

        if (response.status == 200) {
            if (data.role === 'admin') {
                const monit = await fetch('http://localhost:8080/monit')

                const monitList = await monit.json()
                // console.log(monitList.length)

                for (let i = 0; i < monitList.data[0].length; i++) {
                    const records = await fetch('http://localhost:8080/record/code/' + monitList.data[0][i].code)
                    const temp = await records.json()
                    
                    if (temp.code == 200) {
                        monitList.data[0][i].recordN = temp.data[0].length
                    } else {
                        monitList.data[0][i].recordN = 0
                    }
                    
                }

                return {
                    props: {
                        monitList: monitList.data[0]
                    }
                }
            } else if (data.role === 'dokter'){
				return {
					status: 302,
					redirect: '/dokter'
				}
			} else {
                return {
                    status: 403,
                    error: 'Akun anda tidak memiliki akses terhadap halaman ini.'
                }
            }
        } else {
            return {
                status: 302,
                redirect: '/login'
            }
        }
    }
</script>

<svelte:head>
	<title>Form Monitoring</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
    <!-- Table -->
    <div class="w-full overflow-hidden rounded-lg shadow-xs">
		<div class="w-full overflow-x-auto">
			<table class="w-full whitespace-no-wrap border border-neutral-200 table-fixed border-collapse">
				<thead>
					<tr
						class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
					>
						<th class="px-4 py-3 border border-neutral-200">Nama</th>
                        <th class="px-4 py-3 border border-neutral-200">Host</th>
						<th class="px-4 py-3 border border-neutral-200">Jumlah Pasien</th>
						<th class="px-4 py-3 border border-neutral-200">Respon</th>
					</tr>
				</thead>
				{#each monitList as monit}
					<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
					<tr class="text-gray-700 dark:text-gray-400">
						<td class="px-4 py-3 border border-neutral-200">
							<a href="/admin/monitoring/{ monit.code }" class="font-semibold text-sm">{ monit.name }</a>
						</td>
                        <td class="px-4 py-3 text-sm border border-neutral-200">
                            <a href="/admin/dokter/{ monit.host }">{ monit.host }</a>
                        </td>
                        <td class="px-4 py-3 text-sm border border-neutral-200">{ monit.participants.length }</td>
						<td class="px-4 py-3 text-sm border border-neutral-200">{ monit.recordN }</td>
					</tr>
				</tbody>
				{/each }
			</table>
		</div>
	</div>
</div>