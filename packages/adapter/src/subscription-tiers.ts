// Facet subscription tier catalog.
//
// Tier to monthly price, Stripe price id, and rate-limit multiplier.
// Consumed by both the Terminal (tier/price lookup in the Stripe webhook
// and Checkout session route) and the billing UI (plan cards). These
// mirror the marketing rate card: Starter / Pro / Pro+ / Enterprise.
//
// Dual-mode Stripe ids: `stripePriceId` and `stripePriceIdLive` hold the
// test-mode and live-mode price ids respectively. `STRIPE_PRICE_TO_TIER`
// maps inbound webhook events from either mode back to a tier.

export type SubscriptionTier = "starter" | "pro" | "pro_plus" | "enterprise";

export interface SubscriptionTierDefinition {
  readonly tier: SubscriptionTier;
  readonly name: string;
  readonly monthlyPriceMinor: number;
  readonly currency: "USD";
  // Terminal multiplies the default rate-limit ceiling by this.
  // Mirrors the per-tier rate-limit multiplier default.
  readonly rateLimitMultiplier: number;
  // Stripe price id (test-mode). Every tier is paid, so all carry a price.
  readonly stripePriceId: string | null;
  // Stripe price id (live-mode). Used by the webhook handler's reverse
  // map so live-mode subscription events route to the correct tier.
  readonly stripePriceIdLive: string | null;
  // Monthly agent-request cap. Display metadata only: it is not enforced
  // at runtime (the live gate is the hourly rate-limit). Null = no cap.
  readonly monthlyBotCap: number | null;
  // Free-trial length in days before the first charge. Null = no trial.
  // The Terminal passes this as Stripe `trial_period_days` at checkout, so
  // the card is collected up front but not charged until the trial elapses.
  readonly trialDays: number | null;
  readonly features: readonly string[];
}

export const SUBSCRIPTION_TIERS: Readonly<Record<SubscriptionTier, SubscriptionTierDefinition>> = {
  starter: {
    tier: "starter",
    name: "Starter",
    monthlyPriceMinor: 4_900,
    currency: "USD",
    rateLimitMultiplier: 1.0,
    stripePriceId: "price_1U4tkO1C5HQZSKQl0kxOwq3F",
    stripePriceIdLive: "price_1U4u360BCuK3yfzuo6Lk0CQA",
    monthlyBotCap: 40_000,
    trialDays: 30,
    features: [
      "Free for 30 days, then $49/month",
      "40,000 agent queries / month",
      "1,000 requests/hour burst limit",
      "Core Facet protocol endpoints",
      "Public agent reputation API",
      "Catalog changes feed",
    ],
  },
  pro: {
    tier: "pro",
    name: "Pro",
    monthlyPriceMinor: 19_900,
    currency: "USD",
    rateLimitMultiplier: 2.0,
    stripePriceId: "price_1U4tm71C5HQZSKQlaq6kbehN",
    stripePriceIdLive: "price_1U4u470BCuK3yfzu5r2alC3o",
    monthlyBotCap: null,
    trialDays: null,
    features: [
      "Unmetered agent queries",
      "2,000 requests/hour burst limit (2x base)",
      "Everything in Starter",
      "Webhook event delivery",
      "Priority email support",
      "Custom agents.txt fields",
    ],
  },
  pro_plus: {
    tier: "pro_plus",
    name: "Pro+",
    monthlyPriceMinor: 79_900,
    currency: "USD",
    rateLimitMultiplier: 3.0,
    stripePriceId: "price_1U4tmn1C5HQZSKQlI8rjKeTH",
    stripePriceIdLive: "price_1U4u5K0BCuK3yfzuSVhACfTr",
    monthlyBotCap: null,
    trialDays: null,
    features: [
      "Unmetered agent queries",
      "3,000 requests/hour burst limit (3x base)",
      "Everything in Pro",
      "Advanced analytics",
      "Custom domains + SLA",
      "Content licensing",
    ],
  },
  enterprise: {
    tier: "enterprise",
    name: "Enterprise",
    monthlyPriceMinor: 200_000,
    currency: "USD",
    rateLimitMultiplier: 5.0,
    stripePriceId: "price_1U4v9w1C5HQZSKQlqnuFWPxo",
    stripePriceIdLive: "price_1U4vBT0BCuK3yfzuUbEF3Ha1",
    monthlyBotCap: null,
    trialDays: null,
    features: [
      "Unmetered agent queries",
      "5,000 requests/hour burst limit (5x base)",
      "Everything in Pro+",
      "SLA-backed uptime commitments",
      "Dedicated onboarding + account manager",
      "Custom rate-limit tuning",
    ],
  },
};

// Reverse lookup: Stripe price id to tier. The Stripe webhook handler
// consults this map to decide which tier to upgrade a site to on
// `checkout.session.completed`. Both test and live price ids are
// registered so subscriptions from either Stripe mode resolve
// correctly. An unknown price id signals drift between the codebase and
// Stripe; the handler logs and ignores it.
export const STRIPE_PRICE_TO_TIER: Readonly<Record<string, SubscriptionTier>> = {
  [SUBSCRIPTION_TIERS.starter.stripePriceId!]: "starter",
  [SUBSCRIPTION_TIERS.starter.stripePriceIdLive!]: "starter",
  [SUBSCRIPTION_TIERS.pro.stripePriceId!]: "pro",
  [SUBSCRIPTION_TIERS.pro.stripePriceIdLive!]: "pro",
  [SUBSCRIPTION_TIERS.pro_plus.stripePriceId!]: "pro_plus",
  [SUBSCRIPTION_TIERS.pro_plus.stripePriceIdLive!]: "pro_plus",
  [SUBSCRIPTION_TIERS.enterprise.stripePriceId!]: "enterprise",
  [SUBSCRIPTION_TIERS.enterprise.stripePriceIdLive!]: "enterprise",
};
