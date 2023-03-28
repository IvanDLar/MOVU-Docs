# Database Design

Created: March 1, 2023 7:25 PM
Last edited time: March 14, 2023 5:48 PM
Tags: document

[nds | DrawSQL](https://drawsql.app/teams/tec-de-monterrey-3/diagrams/nds)

## Data Model

[https://www.notion.so](https://www.notion.so)

| users |
| --- |
| id: text |
| email: text |
| verified: boolean |
| name: text |
| last_name: text |
| profile_pic_url: text |
| created_at: timestamp |

| user_roles |
| --- |
| id: bigint |
| user_id: text |
| role: text |
| dealer_id: text |
| autogroup_id: text |
| prev: text |

| test_drives |
| --- |
| id: bigint |
| listing_id: bigint |
| driver_id: text |
| date: timestamp |
| documents: jsonb |
| status: text |
| created: timestamp |
| salesman_id: text |

| autogroup |
| --- |
| id: bigint |
| name: text |
| status: int |
| created_at: timestamp |
| enabled_at: timestamp |
| docs: json |
| active: boolean |

| brand |
| --- |
| id: bigint |
| name: text |
| logo: text |

| brand_dealer |
| --- |
| id: bigint |
| brand_id: bigint |
| dealer_id: bigint |

| dealer |
| --- |
| id: bigint |
| name: text |
| url: text |
| logo: text |
| autogroup_id: bigint |
| created_at: timestamp |
| address: text |
| purchase_requirements: jsonb |

| car |
| --- |
| id: bigint |
| brand_id: bigint |
| model: text |
| year: int |
| spec_sheet: text  |
| type: text |
| description: text |

| car_variant |
| --- |
| id: bigint |
| name: text |
| order: int |
| engine: text |
| doors: int |
| description: text |
| hp: bigint |
| engine_liters: bigint |
| turbo: boolean |
| torque: double precision |
| seats: bigint |
| seats_type: text |
| car_id: bigint |
| colors: json |
| colors: json |
| media: json |

| listing |
| --- |
| id: bigint |
| car_id: bigint |
| dealer_id: bigint |
| starting_price: double precision |
| variants: jsonb |
| thumbnail_url: text |

| payment_plans |
| --- |
| id: bigint |
| dealer_id: bigint |
| name: text |
| description: text |
| months: int |
| apr: double precision |
| min_price: double precision |

| order |
| --- |
| id: bigint |
| listing_id: bigint |
| status: text |
| seller_id: text |
| subtotal: double precision |
| configuration: jsonb |
| variant_id: bigint |
| chat_id: bigint |
| payment_plan: bigint |
| buyer_id: text |
| created: timestamp |
| due: double precision |
| insurance_plan: bigint? |

| chat_messages |
| --- |
| id: bigint |
| chat_id: bigint |
| from: text |
| sent: timestamp |
| message: text |

| chats |
| --- |
| id: bigint |
| from: text |
| to: text |
| started: timestamp |
| active: boolean |
| last_active: timestamp |

| business_account_request |
| --- |
| id: bigint |
| status: string |
| created_at: timestamp |
|  |
|  |
|  |