---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/mozambique-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners and clusters
    url: https://data.humdata.org/dataset/mozambique-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/mozambique-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/mozambique-humanitarian-needs
dataset_id: rdls_lss-moz_ochahpc_needs_2022
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The dataset aggregates humanitarian needs assessments compiled by UNOCHA
    on behalf of the Humanitarian Country Team, integrating multi-sector cluster analyses
    to estimate populations in need across Mozambique. Data is disaggregated by administrative
    divisions (Admin 1 and Admin 2), humanitarian sectors, and hazard triggers (conflict
    and natural disasters including flood and drought). The consolidated evidence
    base supports joint strategic response planning through annual HPC cycles (2022-2026).
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners and clusters
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance due to natural disasters
      including flooding
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance due to natural disasters
      including drought
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
        type: total
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
  url: https://analysis.jiaf.info/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/6ad18c3d-f666-4fff-bbd7-d99bea40027d/download/moz_hpc_needs_api_2026.csv
  format: null
  id: resource_6ad18c3d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/89872afa-8893-4c2d-bcef-eeffdc99284c/download/moz_hpc_needs_api_2025.csv
  format: null
  id: resource_89872afa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/290c044b-81a4-4c05-a713-61dd86e8d769/download/moz_hpc_needs_api_2024.csv
  format: null
  id: resource_290c044b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mozambique Humanitarian Needs 2024 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/a5818b13-9207-46cb-bf5f-e8c3dec4b0ba/download/moz_2024_hpc_data_pins_targets_sev_20231206_final.xlsx
  format: null
  id: resource_a5818b13
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mozambique Humanitarian Needs 2023 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/99f3f0b4-856d-41e5-9fd3-588a05e8f019/download/mozambique_hno_hrp-2023-dataset_20221215.xlsx
  format: null
  id: resource_99f3f0b4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mozambique Humanitarian Needs 2022 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/f0081e1f-05fa-4d84-8541-ef477612fc67/resource/a58ede56-0a27-48dd-93c7-d166db5ea365/download/hno_hrp-and-gombe_erp_2022.xlsx
  format: null
  id: resource_a58ede56
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_hpc_needs_2022.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_ochahpc_needs_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: 'Mozambique: Humanitarian Needs'
version: null
vulnerability: null
---
