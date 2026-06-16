---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/cabo-verde-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/cabo-verde-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/cabo-verde-acute-food-insecurity-country-data
dataset_id: rdls_lss-cpv_ipc_acuteinsecuritycountrydat_2022
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cabo-verde-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from the National IPC Technical Working Group to classify populations into five
    phases of food insecurity severity. Population figures are based on official country
    estimates and IPC reports, with spatial disaggregation at national and sub-national
    (area) levels. The dataset represents post-assessment impact classifications used
    for humanitarian decision-making.
  sources:
  - id: source_1
    license: null
    name: National IPC Technical Working Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cabo-verde-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
      food insecurity severity linked to drought and livelihood stress
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
  url: https://www.ipcinfo.org/ipc/technical/manual_en
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/8ea040f1-aa9a-4466-ab6d-7efc3349eec4/download/ipc_cpv.geojson
  format: null
  id: resource_8ea040f1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/e5702a55-8c38-4474-8b34-34e723e044ad/download/ipc_cpv_national_long_latest.csv
  format: null
  id: resource_e5702a55
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/7e85eaf1-8c4a-478f-a36b-5e82126f8f2f/download/ipc_cpv_national_long.csv
  format: null
  id: resource_7e85eaf1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/12469c16-6fb7-481e-b29b-91807092e3a2/download/ipc_cpv_national_wide.csv
  format: null
  id: resource_12469c16
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/be9fad0a-84d1-4816-9e6d-d8a448c75c70/download/ipc_cpv_area_long.csv
  format: null
  id: resource_be9fad0a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cabo Verde: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/b4f5c7ba-3731-4e34-a62b-55fb62d4c887/resource/668a06af-4267-4ef9-9c84-4b3b5ce6ee95/download/ipc_cpv_area_wide.csv
  format: null
  id: resource_668a06af
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cpv_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cpv_ipc_acuteinsecuritycountrydat_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2022-03-01'
temporal_resolution: null
title: 'Cabo Verde: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
