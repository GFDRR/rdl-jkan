---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-som_ochasom_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessments from multiple
    humanitarian partners in Somalia, processed through the Joint Intersectoral Analysis
    Framework (JIAF) methodology to produce intersectoral people in need (PiN) counts
    and severity phase classifications by administrative division and population group.
    The JIAF analysis integrates sectoral assessments, calculates correlation coefficients
    between sectors, and identifies overlapping and highest-impact sectoral needs
    to generate comprehensive humanitarian needs overview data.
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
- href: https://data.humdata.org/dataset/som-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across multiple sectors affected by humanitarian crisis
      in Somalia
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
  - asset_category: population
    asset_dimension: population
    description: Intersectoral severity classification of affected population by administrative
      division
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: JIAF Humanitarian Needs People in Need and Severity (SOM
    - JIAF Humanitarian Needs People in Need and Severity 2026)'
  download_url: https://data.humdata.org/dataset/6ef6efed-56e5-49a2-8640-11fa43fbf8e4/resource/db879fca-246e-41d1-9d21-f332625ce2be/download/jiaf_somalia_2026.xlsx
  format: null
  id: resource_db879fca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SOM_Humanitarian_Needs_PiN_and_Severity_2026
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: JIAF Humanitarian Needs People in Need and Severity (SOM
    - JIAF Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/6ef6efed-56e5-49a2-8640-11fa43fbf8e4/resource/93effff0-912e-4c85-af57-3e5c185039b3/download/jiaf_somalia_2025.xlsx
  format: null
  id: resource_93effff0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SOM_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: JIAF Humanitarian Needs People in Need and Severity (JIAF
    Methodology)'
  download_url: https://data.humdata.org/dataset/6ef6efed-56e5-49a2-8640-11fa43fbf8e4/resource/242c46ce-ec62-4799-9fef-dde94d46d9ed/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_242c46ce
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF-2-Technical-Manual_Final-for-2025-HPC
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_ochasom_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Somalia: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
