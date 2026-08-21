import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

// Release invariant: the package manifest version must match the newest dated
// entry in this package's CHANGELOG, so a version bump can never ship without a
// matching changelog section (and vice versa). Both paths are anchored to this
// file's own location, so the check does not depend on the working directory.
const pkg = JSON.parse(
  readFileSync(fileURLToPath(new URL("../package.json", import.meta.url)), "utf8"),
) as { version: string };
const changelog = readFileSync(fileURLToPath(new URL("../CHANGELOG.md", import.meta.url)), "utf8");

describe("release version", () => {
  it("matches the newest dated CHANGELOG entry", () => {
    const match = changelog.match(/^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}/m);
    expect(match?.[1]).toBe(pkg.version);
  });
});
