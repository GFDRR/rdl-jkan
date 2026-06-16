---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners (multi-agency)
    url: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-tcd_ochatcd_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessments from multiple
    sectoral partners in Chad using the Joint Intersectoral Analysis Framework (JIAF),
    a standardized methodology for analyzing humanitarian needs across sectors and
    administrative divisions. People in need (PiN) figures and intersectoral severity
    classifications are compiled at sub-national levels with correlation coefficients
    and overlap analysis to identify priority areas for humanitarian response.
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
    name: Humanitarian partners (multi-agency)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tcd-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need (PiN) from multiple humanitarian sectors affected
      by various hazards including flooding
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
    description: People in need (PiN) from multiple humanitarian sectors affected
      by drought and food insecurity
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
  - asset_category: population
    asset_dimension: population
    description: People in need (PiN) from multiple humanitarian sectors affected
      by conflict and displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
  description: 'Chad: JIAF Humanitarian Needs People in Need and Severity (TCD - JIAF
    Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/b53eefbf-463b-436c-8c23-72a1c0398cae/resource/02eb7605-8d79-4481-bdd4-de98ab11f17f/download/jiaf_chad_2025.xlsx
  format: null
  id: resource_02eb7605
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: JIAF Humanitarian Needs People in Need and Severity (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/b53eefbf-463b-436c-8c23-72a1c0398cae/resource/d30d01f9-7ff3-4636-8099-f4c7c384ee5c/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_d30d01f9
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
  description: 'Chad: JIAF Humanitarian Needs People in Need and Severity (Hxlated
    version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/b53eefbf-463b-436c-8c23-72a1c0398cae/resource/27f22d3a-e465-4523-8ff8-bdb6c3c5cef8/download/jiaf_chad_2025_hxl.csv
  format: null
  id: resource_27f22d3a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_Chad_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_ochatcd_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-08'
  start: '2025-01-01'
temporal_resolution: null
title: 'Chad: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
