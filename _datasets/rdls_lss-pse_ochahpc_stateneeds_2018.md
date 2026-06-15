---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/opt-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team and partners
    url: https://data.humdata.org/dataset/opt-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/opt-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/opt-humanitarian-needs
dataset_id: rdls_lss-pse_ochahpc_stateneeds_2018
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/opt-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs data compiled by UNOCHA from multiple humanitarian
    partners through the Humanitarian Country Team assessment process. Data includes
    population estimates from Palestinian Central Bureau of Statistics (PCBS) and
    sectoral severity scores aggregated across health, protection, shelter, and WASH
    sectors to estimate people in need (PIN) by governorate and region.
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
    name: Humanitarian Country Team and partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/opt-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across all sectors due to humanitarian crisis in State
      of Palestine
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  url: https://www.ochaopt.org/sites/default/files/HNO_2022.pdf?_gl=1*1agghlz*_ga*MTM1OTE0OTg2NS4xNjY0MTc2NTA4*_ga_E60ZNX2F68*MTY2OTgwNjQwOC4xMjguMS4xNjY5ODExNjc4LjE0LjAuMA
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2023 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/aca411dc-d2ca-4931-b65c-f4a2ed37f3ae/resource/543f6724-c861-4d65-8be4-165745359ae8/download/hno-23_-inter-cluster-pin-collation-sheet.xlsx
  format: null
  id: resource_543f6724
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2022 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/aca411dc-d2ca-4931-b65c-f4a2ed37f3ae/resource/a021fe95-0b35-479e-810f-5ca9341d0019/download/master_hno_2022_statistics.xlsx
  format: null
  id: resource_a021fe95
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2021 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/aca411dc-d2ca-4931-b65c-f4a2ed37f3ae/resource/67f3f997-4d08-48bd-8898-ce137785f312/download/hno_data_admin1_gender_age_disaggregated_april2021.xlsx
  format: null
  id: resource_67f3f997
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2020 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/aca411dc-d2ca-4931-b65c-f4a2ed37f3ae/resource/3c6caca6-f6fc-4a76-a25c-e118a2d3459a/download/opt_hno_2020.xlsx
  format: null
  id: resource_3c6caca6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2019 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vRprDPPizjr4mNb2XVvDTuBalq6oYakRVX3tbXqwikc87AolVC6m6J35JcW61jBJIkWjI05ZB_CY5OJ/pub?output=xlsx
  format: null
  id: resource_6b4d097a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The State of Palestine Humanitarian Needs 2018 dataset was compiled
    by OCHA on behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/aca411dc-d2ca-4931-b65c-f4a2ed37f3ae/resource/264a04c8-6024-40b0-b3fc-113152e3f48a/download/hno_opt_2018.xlsx
  format: null
  id: resource_264a04c8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_hpc_needs_2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_ochahpc_stateneeds_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'State of Palestine: Humanitarian Needs'
version: null
vulnerability: null
---
