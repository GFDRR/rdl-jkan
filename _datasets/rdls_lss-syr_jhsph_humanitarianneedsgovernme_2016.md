---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/humanitarian-needs-in-government-controlled-areas-of-syria
creator:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/humanitarian-needs-in-government-controlled-areas-of-syria
dataset_id: rdls_lss-syr_jhsph_humanitarianneedsgovernme_2016
description: 'This is the underlying data for a manuscript published in PLOS: Currents
  Disasters. The manuscript reports results from a survey of accessible areas, which
  were largely urban and government controlled, undertaken from April - June 2016
  to identify unmet needs and assistance priorities in Syria.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/humanitarian-needs-in-government-controlled-areas-of-syria]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: A cross-sectional survey was conducted in accessible government-controlled
    areas of Syria (April-June 2016) to identify unmet humanitarian needs and assistance
    priorities among affected populations. Survey data were compiled into a structured
    dataset documenting needs assessments across sampled locations, serving as empirical
    loss/impact data for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: Johns Hopkins School of Public Health
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/humanitarian-needs-in-government-controlled-areas-of-syria
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Unmet humanitarian needs and assistance priorities among affected
      population in government-controlled areas of Syria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Humanitarian Needs in Government Controlled Areas of Syria (IOCC PLOS
    Minimal Underlying Dataset.xls)
  download_url: https://data.humdata.org/dataset/1c8ddca6-81b7-4217-bafb-d3c2236780fe/resource/95b64b9f-9ba0-403b-a644-c6e5c94c9334/download/iocc-plos-minimal-underlying-dataset.xls
  format: null
  id: resource_95b64b9f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IOCC PLOS Minimal Underlying Dataset.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_jhsph_humanitarianneedsgovernme_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-06-01'
  start: '2016-04-01'
temporal_resolution: null
title: Humanitarian Needs in Government Controlled Areas of Syria
version: null
vulnerability: null
---
