---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/bangladesh-displacement-idps-estimate-of-internally-displaced-persons-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/bangladesh-displacement-idps-estimate-of-internally-displaced-persons-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/bangladesh-displacement-idps-estimate-of-internally-displaced-persons-iom-dtm
dataset_id: rdls_lss-bgd_iom_displacementidpsestimatei_2025
description: 'Bangladesh is highly vulnerable to recurrent natural hazards including
  cyclones, floods, tidal surges, landslides, and riverbank erosion which continue
  to trigger widespread internal displacement. Despite the persistent nature of these
  hazards, the country has historically lacked a comprehensive, nationwide estimate
  of the total number of IDPs affected by disasters. Existing data has largely been
  fragmented, event-specific, or geographically limited, making it difficult for policymakers
  to understand the scale and patterns of displacement or plan nation-wide responses.
  Recognizing this long-standing data gap, the International Organization for Migration
  (IOM) undertook Bangladesh''s first systematic national IDP estimation exercise
  using the Displacement Tracking Matrix (DTM) methodology. This assessment applied
  a structured approach to identify displacement across all 5,388 administrative units
  of Bangladesh. This nationwide assessment builds upon and supports the Government
  of Bangladesh''s National Strategy on Internal Displacement Management by operationalizing
  ''Activity 2.1.1'', which mandates systematic and periodic collection of field-level
  displacement data under the guidance of the Ministry of Disaster Management and
  Relief (MoDMR) and local institutional structures. The initiative was supported
  through multiple IOM projects funded by the European Union (EU), the IOM Development
  Fund (IDF), and the Norwegian Agency for Development Cooperation (NORAD) via the
  Platform on Disaster Displacement (PDD), reflecting strong international collaboration
  in strengthening Bangladesh''s displacement data ecosystem. By providing a clear
  and verified national estimate, this assessment will help the government and partners
  make better decisions on disaster preparedness, social protection, relocation planning,
  and long-term development.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-displacement-idps-estimate-of-internally-displaced-persons-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted nationwide displacement tracking surveys across Bangladesh
    administrative divisions (Division, District, Upazila) to estimate the total number
    of internally displaced persons affected by recurrent natural hazards. Data was
    collected and aggregated using DTM standard methodology to provide comprehensive,
    geographically-disaggregated IDP estimates by hazard type and administrative location.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bangladesh-displacement-idps-estimate-of-internally-displaced-persons-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from cyclones and tropical storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
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
    description: Internally displaced persons from fluvial and pluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
    description: Internally displaced persons from tidal surges and coastal flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
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
    description: Internally displaced persons from landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
    description: Internally displaced persons from riverbank erosion
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_erosion
      intensity_measure: Er:T/ha
      process: null
      trigger: null
      type: erosion
    id: loss_5
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This assessment was carried out across all eight divisions, 64 districts
    and 12 City Corporations of Bangladesh, covering 4,579 unions, 329 municipalities
    and 480 City Corporation wards. Data collection took place between September and
    October 2025, during which 6,524 collective interviews were conducted with 29,117
    key informants, making this the most comprehensive national assessment of disaster-induced
    internal displacement in Bangladesh.
  download_url: https://data.humdata.org/dataset/f563ae50-58c0-4a67-b2a6-8df0679bad8d/resource/41f4c6ed-a4cc-447a-b16c-0411c907e9a5/download/bangladesh_idps_estimate_round_1_october_2025_hdx.xlsx
  format: null
  id: resource_41f4c6ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bangladesh - DPs Estimate - Round 1 - October 2025
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_iom_displacementidpsestimatei_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '2025-09-01'
temporal_resolution: null
title: Bangladesh Displacement - [IDPs] - Estimate of Internally Displaced Persons
  [IOM DTM]
version: null
vulnerability: null
---
