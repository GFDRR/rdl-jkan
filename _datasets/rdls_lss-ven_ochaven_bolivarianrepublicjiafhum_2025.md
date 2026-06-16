---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Venezuela
  url: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Venezuela
  url: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-ven_ochaven_bolivarianrepublicjiafhum_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian partners conducted sectoral needs assessments across Venezuela's
    administrative divisions using the Joint Intersectoral Analysis Framework (JIAF)
    methodology. OCHA integrated these sectoral inputs (food security, nutrition,
    health, WASH, shelter, education, protection) to produce intersectoral severity
    scores and final people in need estimates at admin 1 and admin 2 levels.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ven-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across multiple sectors (food security, nutrition,
      health, WASH, shelter, education, protection) assessed through intersectoral
      analysis
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Venezuela (Bolivarian Republic of): JIAF Humanitarian Needs People
    in Need and Severity (VEN- JIAF Humanitarian Needs People in Need and Severity
    2025)'
  download_url: https://data.humdata.org/dataset/5cdf5c58-9b03-4bab-ad08-d455e421bea9/resource/3a5050c3-45ea-4e83-a491-4493c486a983/download/jiaf_venezuela_2025.xlsx
  format: null
  id: resource_3a5050c3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VEN_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Venezuela (Bolivarian Republic of): JIAF Humanitarian Needs People
    in Need and Severity (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/5cdf5c58-9b03-4bab-ad08-d455e421bea9/resource/0496ee8b-de88-496a-81bc-0affbbdc75ae/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_0496ee8b
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
  description: 'Venezuela (Bolivarian Republic of): JIAF Humanitarian Needs People
    in Need and Severity (Hxlated version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/5cdf5c58-9b03-4bab-ad08-d455e421bea9/resource/24d59616-8248-4a56-8a53-fe2339c1c225/download/jiaf_venezuela_2025_hxl.csv
  format: null
  id: resource_24d59616
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_Venezuela_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ven_ochaven_bolivarianrepublicjiafhum_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Venezuela (Bolivarian Republic of): JIAF Humanitarian Needs People in Need
  and Severity'
version: null
vulnerability: null
---
