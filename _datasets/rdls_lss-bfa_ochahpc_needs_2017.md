---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/burkina-faso-humanitarian-needs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/burkina-faso-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/burkina-faso-humanitarian-needs
dataset_id: rdls_lss-bfa_ochahpc_needs_2017
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-faso-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOCHA compiled humanitarian needs data from multiple humanitarian
    partners through the Humanitarian Country Team coordination process. Data aggregates
    people-in-need figures by administrative level, cluster, and category across multiple
    years (2017-2026), representing consolidated humanitarian impact assessments rather
    than post-event damage surveys.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-faso-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need due to drought-driven humanitarian crisis in Burkina
      Faso
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  url: https://reliefweb.int/attachments/fed38dad-d42b-43fd-9a2e-6a9924e2c8e4/BFA_HPC_2023_HNO_mars_compressed%20%282%29.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/bb442035-b2d5-41c7-b5c9-00ead83f6bb8/download/bfa_hpc_needs_api_2026.csv
  format: null
  id: resource_bb442035
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/6cf853b1-9f34-407b-851c-201e83432dce/download/bfa_hpc_needs_api_2025.csv
  format: null
  id: resource_6cf853b1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/50059eac-a9b9-4054-a8de-261483cd7a17/download/bfa_hpc_needs_api_2024.csv
  format: null
  id: resource_50059eac
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Burkina Faso Humanitarian Needs 2024 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/bfc5a2d0-23e7-46e7-bde4-1a3a54f45d8e/download/bfa_hno_2024.xlsx
  format: null
  id: resource_bfc5a2d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Burkina Faso Humanitarian Needs 2023 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/dbc091a9-d3db-412c-a955-feb18ae1be48/download/bf-hpc-2023-pin-intercluster-and-clusters.xlsx
  format: null
  id: resource_dbc091a9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Burkina Faso Humanitarian Needs 2022 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/5a487aa4-f044-439e-9a5f-26e6d7fa9948/download/bfa-pin-20222-dakar.xlsx
  format: null
  id: resource_5a487aa4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Burkina Faso Humanitarian Needs 2021 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/2254ea6a-53fa-40c9-b206-43d819e00344/download/bfa_hno_2021.xlsx
  format: null
  id: resource_2254ea6a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Burkina Faso Humanitarian Needs 2017 dataset was compiled by OCHA
    on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/d5a68479-9c34-490e-850a-5329ef056662/resource/07f9e557-db9e-459c-ba70-61a0a423f166/download/bfa_hno_2017.xlsx
  format: null
  id: resource_07f9e557
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hpc_needs_2017
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ochahpc_needs_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Burkina Faso: Humanitarian Needs'
version: null
vulnerability: null
---
