<script>
    import NoEntry from '../../components/admin/NoEntry.svelte';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../stores/admin.js';
	import { parseDate } from '$lib/date.js'

	onMount(async () => {
		pageName.update(() => document.title);
	});

    export let userList, totalMonit, totalRecords

    var rez={};
    userList.forEach(function(user){
        rez[user.role] ? rez[user.role]++ :  rez[user.role] = 1;
    });
    console.log(rez);

    // console.log(userList)
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
                const users = await fetch('http://localhost:8003/api/users')
                const records = await fetch('http://localhost:8080/record')
                const monit = await fetch('http://localhost:8080/monit')

                const userList = await users.json()
                const recordList = await records.json()
                const monitList = await monit.json()

                
                if (userList) {
					userList.sort(function(a,b) {
						const keyA = new Date(a.lastLoginDate), keyB = new Date(b.lastLoginDate);
						if (keyA > keyB) return -1;
						if (keyA < keyB) return 1;
						return 0;
					})
				}
                return {
                    props: {
                        userList: userList,
                        totalRecords: recordList.data[0].length,
                        totalMonit: monitList.data[0].length
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
	<title>Dashboard</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
    <!-- Cards -->
    <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
        <!-- Card pasien-->
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
				<a href="/admin/pasien"><p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Jumlah Pasien</p></a>
				<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{ rez.pasien }</p>
			</div>
		</div>
        <!-- Card Dokter -->
		<div
			class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
		>
			<div
				class="p-3 mr-4 text-purple-500 bg-purple-100 rounded-full dark:text-green-100 dark:bg-green-500"
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
				<a href="/admin/dokter"><p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Jumlah Dokter</p></a>
				<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{ rez.dokter }</p>
			</div>
		</div>
        <!-- Card Monitoring -->
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
				<a href="/admin/monitoring"><p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Monitoring Form</p></a>
				<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{ totalMonit }</p>
			</div>
		</div>
        <!-- Card Respon -->
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
				<a href="/admin/responds"><p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Jumlah Respon</p></a>
				<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{ totalRecords }</p>
			</div>
		</div>
    </div>

    <!-- Recent Logins -->
    <div>
        <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Login Terakhir</h4>

        <div class="w-full overflow-hidden rounded-lg shadow-xs">
			<div class="w-full overflow-x-auto">
				<table class="w-full whitespace-no-wrap border border-neutral-200">
					<thead>
						<tr
							class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
						>
							<th class="px-4 py-3">Username</th>
							<th class="px-4 py-3">Role</th>
							<th class="px-4 py-3">Tanggal</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
                        {#each userList as user}
						<!-- {#each recordList as record} -->
						<tr class="text-gray-700 dark:text-gray-400">
							<td class="px-4 py-3 text-sm">
                                {#if user.role === 'dokter'}
                                    <a href="/admin/dokter/{ user.username }"><p class="font-semibold">{ user.username }</p></a>
                                {:else if user.role === 'pasien'}
                                    <a href="/admin/pasien/{ user.username }"><p class="font-semibold">{ user.username }</p></a>
                                {:else if user.role === 'admin'}
                                    <p class="font-semibold">{ user.username }</p>
                                {/if}
								
							</td>
							<td class="px-4 py-3 text-sm">{ user.role[0].toUpperCase() + user.role.substring(1) }</td>

							<td class="px-4 py-3 text-sm">{ parseDate(user.lastLoginDate) }</td>
						</tr>
						<!-- {/each} -->
                        {/each}
					</tbody>
				</table>
			</div>
		</div>
    </div>
</div>