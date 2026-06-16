---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-nga_ochanga_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessments from multiple
    partner organizations using the Joint Intersectoral Analysis Framework (JIAF)
    methodology, which synthesizes sectoral and intersectoral analyses to produce
    overall people in need and severity classifications disaggregated by administrative
    divisions and population groups across Nigeria.
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
- href: https://data.humdata.org/dataset/nga-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need and intersectoral severity assessment from multi-hazard
      humanitarian analysis
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
  description: 'Nigeria: JIAF Humanitarian Needs People in Need and Severity (NGA
    - JIAF Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/608e1e20-c459-4afc-9f73-f2ad6ce4d782/resource/b430e409-7870-4673-b1f4-fcd623d3fab8/download/jiaf_nigeria_2025.xlsx
  format: null
  id: resource_b430e409
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: JIAF Humanitarian Needs People in Need and Severity (JIAF
    Methodology)'
  download_url: https://data.humdata.org/dataset/608e1e20-c459-4afc-9f73-f2ad6ce4d782/resource/34dd31cd-477c-4f00-ada6-ae58f3a43d45/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_34dd31cd
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
  description: 'Nigeria: JIAF Humanitarian Needs People in Need and Severity (Hxlated
    version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/608e1e20-c459-4afc-9f73-f2ad6ce4d782/resource/0a11aa8b-da49-4066-b4e7-2ac243717a6a/download/jiaf_nigeria_2025_hxl.csv
  format: null
  id: resource_0a11aa8b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_Nigeria_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_ochanga_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Nigeria: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
