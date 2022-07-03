import { writable } from 'svelte/store';

export const pageName = writable('Dashboard');
export let storeFields = writable([]);
export let monitStore = writable([]);
export let sideMenuOpen = writable(false);
