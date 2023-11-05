# bercerita

## Development Server

There is a Python-based development server that can redirect routes such as `/about`
to `about.html`. To use it, ensure [Python 3](https://www.python.org/) is installed
on your computer.

The server will run on port 8080 by default, but this can be overridden with the
`PORT` environment variable. If port 8080 is not available, the server will iterate
until an available port is found.

### Usage

Run the following command in a terminal in the repository's directory.

```bash
python3 server.py
```

## Tailwind CSS

The donate page uses [Tailwind CSS](https://tailwindcss.com). To compile the page's
CSS, use your preferred package manager (`npm`, `pnpm`, or `yarn`), and run the
`dev:tailwind` or `dev:tailwind:watch` scripts.

### Usage

```bash
npm run dev:tailwind
npm run dev:tailwind:watch
```

```bash
pnpm dev:tailwind
pnpm dev:tailwind:watch
```

```bash
yarn dev:tailwind
yarn dev:tailwind:watch
```
