# Test code templates

Created: March 13, 2023 8:10 PM
Last edited time: March 13, 2023 8:10 PM
Tags: code

**Unit Test Template**:

```tsx
import React from "react";
import { render } from "@testing-library/react";
import TopLevelComponent from "./TopLevelComponent";

jest.mock("./Modal", () => () => {
  return <mock-modal data-testid="modal"/>;
});

test("If TopLevelComponent is passed the open prop Modal is rendered", () => {
  const { queryByTestId } = render(<TopLevelComponent open />);
  expect( queryByTestId("modal") ).toBe(true)
});
```

**Integration Tests Template**:

```tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { loadStripe } from '@stripe/stripe-js';
import { Elements } from '@stripe/react-stripe-js';

import PaymentForm from '../components/PaymentForm';

const stripePromise = loadStripe('your_stripe_publishable_key_here');

describe('PaymentForm Integration Test', () => {
  it('should submit payment details and receive success confirmation from Stripe', async () => {
    // Render the PaymentForm component with Stripe Elements
    render(
      <Elements stripe={stripePromise}>
        <PaymentForm />
      </Elements>
    );

    // Enter payment details into form fields
    const cardInput = screen.getByLabelText('Card number');
    fireEvent.change(cardInput, { target: { value: '4242424242424242' } });

    const expInput = screen.getByLabelText('Expiration date');
    fireEvent.change(expInput, { target: { value: '12/24' } });

    const cvcInput = screen.getByLabelText('CVC');
    fireEvent.change(cvcInput, { target: { value: '123' } });

    const nameInput = screen.getByLabelText('Name on card');
    fireEvent.change(nameInput, { target: { value: 'Test User' } });

    // Submit payment details
    const submitButton = screen.getByRole('button', { name: 'Pay' });
    fireEvent.click(submitButton);

    // Wait for Stripe to process the payment and receive success confirmation
    await waitFor(() => {
      const successMessage = screen.getByText('Payment successful!');
      expect(successMessage).toBeInTheDocument();
    });
  });
});
```

**E2E Tests Template**:

```tsx
describe('My First Test', () => {
  it('Visits the Kitchen Sink', () => {
    cy.visit('https://example.cypress.io')

		cy.contains('Hello World')
  })
})

```