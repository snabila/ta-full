<script>
	import { pageName, sideMenuOpen } from '../../stores/admin.js';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { messageStore } from '../../stores/chat'

	let show = false; // menu state
	let menu = null; // menu wrapper DOM reference

	let displayPageName;

	pageName.subscribe((value) => {
		displayPageName = value;
	});

	let isOpen

	sideMenuOpen.subscribe((value) => {
		isOpen = value;
	});

	onMount(() => {
		const handleOutsideClick = (event) => {
			if (show && !menu.contains(event.target)) {
				show = false;
			}
		};

		const handleEscape = (event) => {
			if (show && event.key === 'Escape') {
				show = false;
			}
		};

		// add events when element is added to the DOM
		document.addEventListener('click', handleOutsideClick, false);
		document.addEventListener('keyup', handleEscape, false);

		// remove events when element is removed from the DOM
		return () => {
			document.removeEventListener('click', handleOutsideClick, false);
			document.removeEventListener('keyup', handleEscape, false);
		};
	});
	
	const logout = async () => {
		await fetch('http://localhost:8080/auth/logout', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		// auth = false
		messageStore.set([])
		await goto('/login')
	}

	function mobileMenuOpen() {
		if (isOpen) {
			$sideMenuOpen = false
		}
		else {
			$sideMenuOpen = true
		}
	}
</script>

<header class="z-10 md:py-4 py-3">
	<div
		class="container flex items-center justify-between h-full md:py-4 py-0 px-6 mx-auto text-neutral-600 dark:text-neutral-300"
	>
		<!-- Title and Mobile menu -->
		<div class="inline-flex items-center">
			<!-- Mobile Hamburger -->
			<button
				class="p-1 mr-5 -ml-1 rounded-md md:hidden focus:outline-none focus:shadow-outline-purple"
				aria-label="Menu"
				on:click={ mobileMenuOpen }
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-6 w-6"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					stroke-width="2"
				>
					<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
				</svg>
			</button>

			<!-- Page title -->
			<h3 class="font-semibold text-lg md:text-2xl">{displayPageName}</h3>
		</div>

		<ul class="flex items-center flex-shrink-0 space-x-6">
			<!-- Profile menu -->
			<li class="relative" bind:this={menu}>
				<button
					class="align-middle rounded-full focus:shadow-outline-purple focus:outline-none"
					aria-label="Account"
					aria-haspopup="true"
					on:click={() => (show = !show)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
						<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd" />
					</svg>
				</button>

				{#if show}
					<div>
						<ul
							x-transition:leave="transition ease-in duration-150"
							x-transition:leave-start="opacity-100"
							x-transition:leave-end="opacity-0"
							class="absolute right-0 w-56 p-2 mt-2 space-y-2 text-gray-600 bg-white border border-gray-100 rounded-md shadow-md dark:border-gray-700 dark:text-gray-300 dark:bg-gray-700"
							aria-label="submenu"
						>
							<!-- <li class="flex">
								<a
									class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
									href="/"
								>
									<svg
										class="w-4 h-4 mr-3"
										aria-hidden="true"
										fill="none"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
									</svg>
									<span>Profile</span>
								</a>
							</li>
							<li class="flex">
								<a
									class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
									href="/"
								>
									<svg
										class="w-4 h-4 mr-3"
										aria-hidden="true"
										fill="none"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<path
											d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
										/>
										<path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
									</svg>
									<span>Settings</span>
								</a>
							</li> -->
							<li class="flex">
								<button
									class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
									href="/"
									on:click={logout}
								>
									<svg
										class="w-4 h-4 mr-3"
										aria-hidden="true"
										fill="none"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<path
											d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
										/>
									</svg>
									<span>Log out</span>
								</button>
							</li>
						</ul>
					</div>
				{/if}
			</li>
		</ul>
	</div>
</header>
