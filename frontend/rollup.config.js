import { config } from 'dotenv';
import replace from '@rollup/plugin-replace';

const configToReplace = {};
for (const [key, v] of Object.entries(config().parsed)) {
	configToReplace[`process.env.${key}`] = `'${v}'`;
}

export default {
	plugins: [
		replace({
			include: ['src/**/*.ts', 'src/**/*.svelte'],
			preventAssignment: true,
			values: configToReplace
		})
	]
};
