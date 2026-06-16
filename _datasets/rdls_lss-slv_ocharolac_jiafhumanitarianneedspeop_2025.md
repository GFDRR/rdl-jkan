---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-slv_ocharolac_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs data collected by multiple humanitarian partners
    in El Salvador were analyzed and aggregated using the Joint Intersectoral Analysis
    Framework (JIAF) methodology developed by OCHA. The framework integrates sectoral
    assessments (food security, protection, WASH, health, nutrition, shelter, education)
    to produce overall people in need (PiN) and intersectoral severity indicators
    disaggregated by administrative divisions and population groups.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/slv-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across multiple sectors (food security, protection,
      WASH, health, nutrition, shelter, education) affected by humanitarian crisis
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'El Salvador: JIAF Humanitarian Needs People in Need and Severity (SLV
    - JIAF Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/c19dd406-4c3d-451f-899c-2b349576fad7/resource/e55342f5-e9b6-4485-a5a8-a16dbd7b35af/download/jiaf_el-salvador_2025.xlsx
  format: null
  id: resource_e55342f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLV_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'El Salvador: JIAF Humanitarian Needs People in Need and Severity (JIAF
    Methodology)'
  download_url: https://data.humdata.org/dataset/c19dd406-4c3d-451f-899c-2b349576fad7/resource/40563ec6-9207-4e7c-aa29-4a316a6e86af/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_40563ec6
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF-2-Technical-Manual_Final-for-2025-HPC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'El Salvador: JIAF Humanitarian Needs People in Need and Severity (Hxlated
    version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/c19dd406-4c3d-451f-899c-2b349576fad7/resource/6d144a51-30a3-4d3f-8245-1af9fb846590/download/jiaf_el-salvador_2025_hxl.csv
  format: null
  id: resource_6d144a51
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_El-Salvador_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-slv_ocharolac_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'El Salvador: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
