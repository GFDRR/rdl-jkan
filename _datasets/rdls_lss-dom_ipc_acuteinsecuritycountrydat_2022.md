---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/dominican-republic-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/dominican-republic-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/dominican-republic-acute-food-insecurity-country-data
dataset_id: rdls_lss-dom_ipc_acuteinsecuritycountrydat_2022
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/dominican-republic-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using the standardized IPC methodology to assess and
    classify population food insecurity phases. Population estimates are based on
    official country census data, and results are disaggregated by administrative
    area and time period (current and projected phases).
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
- href: https://data.humdata.org/dataset/dominican-republic-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
      food insecurity severity linked to drought and other shocks
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
  description: 'Dominican Republic: Acute Food Insecurity Country Data (IPC GeoJSON
    for latest analysis)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/77a7c3b9-e816-49d2-9c07-f3299385fcf4/download/ipc_dom.geojson
  format: null
  id: resource_77a7c3b9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (Latest IPC
    national data in long form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/f63fcd5e-fb71-4de0-b0dd-5cf3dc166512/download/ipc_dom_national_long_latest.csv
  format: null
  id: resource_f63fcd5e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (Latest IPC
    area data in long form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/31c988ee-f1e2-470d-b834-701d8bb87c6a/download/ipc_dom_area_long_latest.csv
  format: null
  id: resource_31c988ee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (Latest IPC
    area data in wide form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/ca4aa7a7-cd02-4304-8c45-16cd9daa8cd6/download/ipc_dom_area_wide_latest.csv
  format: null
  id: resource_ca4aa7a7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/6c6a03f8-e68b-496c-affa-951b67ed2e21/download/ipc_dom_national_long.csv
  format: null
  id: resource_6c6a03f8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/f3ca290d-4568-4e0e-9925-02656716da9c/download/ipc_dom_national_wide.csv
  format: null
  id: resource_f3ca290d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (All IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/f295422d-1b37-412e-b685-b2333ffe7441/download/ipc_dom_area_long.csv
  format: null
  id: resource_f295422d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Acute Food Insecurity Country Data (All IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/ee8f4b48-cef5-4e71-a398-b9d525d7bf00/resource/776f5185-adf5-4b98-904f-d38e675ffbf9/download/ipc_dom_area_wide.csv
  format: null
  id: resource_776f5185
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dom_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-dom_ipc_acuteinsecuritycountrydat_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-09-30'
  start: '2022-10-01'
temporal_resolution: null
title: 'Dominican Republic: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
