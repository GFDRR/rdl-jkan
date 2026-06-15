---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-hnd
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-hnd
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-hnd
dataset_id: rdls_hel-hnd_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-hnd]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population distribution across administrative divisions
      in Honduras
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and international organizations (ACLED, IPC, IOM, UNHCR, WFP, OCHA)
    into a unified API for Honduras. Source data includes conflict event records,
    food security classifications, displacement counts, and baseline population estimates,
    which are harmonized to common administrative boundaries and temporal reference
    periods to enable interoperable humanitarian analysis and decision support.
  sources:
  - id: source_1
    license: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-hnd
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict events in Honduras
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by food insecurity classified by IPC phase
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons in Honduras
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Humanitarian needs population across sectors in Honduras
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "IDPs data from HDX HAPI, please see the documentation for more information\
    \ Source: International Organization for Migration (IOM) License: Copyright \xC2\
    \xA9 International Organization for Migration 2018 IOM reserves the right to assert\
    \ ownership of the Materials collected on the https://data.humdata.org/ website.\
    \ The Materials may be viewed, downloaded, and printed for non-commercial use\
    \ only, without, inter alia, any right to sell, resell, redistribute or create\
    \ derivative works therefrom. At all times the User shall credit the DTM as the\
    \ source, unless otherwise stated. The user must include the URL of the Materials\
    \ from the HDX Website, as well as the following credit line: Source: 'International\
    \ Organization for Migration (IOM), Displacement Tracking Matrix (DTM)'."
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/01b4ce56-7deb-4ddc-a3b1-68f482950ab3/download/hdx_hapi_idps_hnd.csv
  format: null
  id: resource_01b4ce56
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/e63eeb2d-e122-43f9-ad48-49ff3d65c68b/download/hdx_hapi_refugees_hnd.csv
  format: null
  id: resource_e63eeb2d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Humanitarian needs data from HDX HAPI, please see the documentation
    for more information Source: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    License: Creative Commons Attribution for Intergovernmental Organisations (CC
    BY-IGO)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/40b01bed-d2bb-4430-9412-3b8346898f13/download/hdx_hapi_humanitarian_needs_hnd.csv
  format: null
  id: resource_40b01bed
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Humanitarian Needs for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/b3cb8a81-48c0-4a79-84f6-a6786a23f9d5/download/hdx_hapi_funding_hnd.csv
  format: null
  id: resource_b3cb8a81
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/d216be88-8b81-42ec-956e-6ce4eb72e410/download/hdx_hapi_conflict_event_hnd.csv
  format: null
  id: resource_d216be88
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/fe49c106-e0d9-4485-bd78-17b4bae50b29/download/hdx_hapi_national_risk_hnd.csv
  format: null
  id: resource_fe49c106
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Security data from HDX HAPI, please see the documentation for
    more information Source: Integrated Food Security Phase Classification (IPC) License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/04bd8edd-31f2-4342-a8ec-fb4d0445d2e2/download/hdx_hapi_food_security_hnd.csv
  format: null
  id: resource_04bd8edd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Security for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/ed4f6241-31c9-499b-8aa6-3570afe9301d/download/hdx_hapi_food_price_hnd.csv
  format: null
  id: resource_ed4f6241
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/44bae31f-5da1-45ee-82af-e28623ba7c8c/download/hdx_hapi_poverty_rate_hnd.csv
  format: null
  id: resource_44bae31f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/36daf8a9-9097-47b3-a467-ce92f292aa7e/download/hdx_hapi_population_hnd.csv
  format: null
  id: resource_36daf8a9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/b9a1aef6-2432-4b8e-9b40-bb17982889e0/download/hdx_hapi_rainfall_hnd.csv
  format: null
  id: resource_b9a1aef6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Honduras'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/82806f2f-398d-4fa8-b7b2-d099679bd324/resource/f3b6619c-61fd-43e3-839a-e2ee23520ea2/download/hdx_hapi_data_availability_hnd.csv
  format: null
  id: resource_f3b6619c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Honduras'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-hnd_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2027-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Honduras
version: null
vulnerability: null
---
