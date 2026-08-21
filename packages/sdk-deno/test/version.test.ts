// Release self-test: the package version in deno.json must match the
// newest dated release header in CHANGELOG.md. Keeps a version bump and
// its changelog entry from drifting apart. Reads both files relative to
// this module (needs --allow-read).

import { assertEquals } from "jsr:@std/assert@1";

const DATED_RELEASE = /^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}/m;

Deno.test("deno.json version matches the newest dated CHANGELOG.md release", async () => {
  const { version } = JSON.parse(
    await Deno.readTextFile(new URL("../deno.json", import.meta.url)),
  ) as { version: string };

  const changelog = await Deno.readTextFile(new URL("../CHANGELOG.md", import.meta.url));
  const match = changelog.match(DATED_RELEASE);

  assertEquals(
    typeof match?.[1],
    "string",
    "CHANGELOG.md is missing a dated '## [X.Y.Z] - YYYY-MM-DD' release header",
  );
  assertEquals(
    version,
    match?.[1],
    `deno.json version (${version}) must match the newest dated CHANGELOG entry (${match?.[1]})`,
  );
});
