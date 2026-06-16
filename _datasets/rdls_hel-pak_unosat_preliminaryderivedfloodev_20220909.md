---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-9-se
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-9-se
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-9-se
dataset_id: rdls_hel-pak_unosat_preliminaryderivedfloodev_20220909
description: 'UNOSAT code FL20220808PAK, GDACS Id: 1101522 Status: Increasing and
  receding flood waters observed Further action(s): continue monitoring Summary of
  findings; Evolution of Cumulative Flood Impact Assessment (25 - 31 August Vs 01-07
  September 2022): From 01 to 07 September 2022 approximately 22 million people remain
  potentially exposed or living close to flooded areas Based on satellite data from
  25 - 31 August and 01-07 September, flood waters appear to be receding in many parts
  of the country, however, many districts in the southern province of Sindh still
  appear to be heavily affected by flooding and increasing flood waters. Floods assessment
  in Sindh Province Large floods were observed all along the Indus river; Guddu Barrage
  seem to be intact as of 1 Sep. 2022 Inundated villages and inundated agricultural
  areas were observed along Indus river as of 5 Sep. 2022; The increasing floodwater
  along Indus river in Khairpur, Jamshoro, Shaheed Benazir Abad, Thatta and Sujawal
  districts observed as of 5 Sep. 2022;. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-9-se]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed or living close to flooded areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed multi-temporal satellite imagery from 25-31
    August and 01-07 September 2022, comparing successive images to detect flood water
    extent and evolution. Population exposure was derived by overlaying observed flood
    extents with gridded population data to quantify people potentially exposed to
    or living near flooded areas. The assessment tracked cumulative flood impacts
    and water recession patterns across Pakistan during the 2022 monsoon flooding
    event.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-9-se
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood waters during August-September 2022
      Pakistan flooding event
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
        type: direct
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan-9 Sep. 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3350/UNOSAT_Population_Exposure_FL20220808PAK_20220825_20220831_20220901_20220907_Updated14Sep2022.xlsx
  format: null
  id: resource_b365e696
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20220808PAK_20220825_20220831_20220901_20220907_Updated14Sep2022.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_preliminaryderivedfloodev_20220909
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-09-09'
temporal_resolution: null
title: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
  of Pakistan-9 Sep. 2022
version: null
vulnerability: null
---
