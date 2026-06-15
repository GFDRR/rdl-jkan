---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria
dataset_id: rdls_lss-syr_unosat_rapidlyassesseddamageoccu_20180301
description: 'This map illustrates satellite-detected damage in the subdistricts of
  Kafr Batna and Irbin and in the eastern part of Damascus city, Syrian Arab Republic.
  Using satellite imagery collected 23 February 2018 and comparing with imagery acquired
  3 December 2017, UNITAR - UNOSAT conducted a Rapid Damage Assessment, over a total
  area of 62.5 square kilometers, to provide an overview of areas of recent damage.
  The area analyzed was divided in cells and each cell was assessed searching for
  presence of new damage. Our analysis shows that 29% of the cells were affected by
  major new damage, with presence of buildings completely destroyed or severely damaged
  between 3 December 2017 and 23 February 2018. In addition 24% of the cells showed
  signs of minor new damage, with visible impact craters, debris or moderately damaged
  structures. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts compared satellite imagery acquired on 3 December\
    \ 2017 and 23 February 2018 over a 62.5 km\xC2\xB2 study area in Eastern Ghouta\
    \ and Damascus, Syria. The area was divided into grid cells and each cell was\
    \ assessed for presence of new damage, with damage classified by confidence level\
    \ and severity. Results quantify the proportion of cells affected by major damage\
    \ (29%) as a post-event impact assessment."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed through satellite imagery comparison
      between December 2017 and February 2018
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
        metric: loss
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
  description: Rapidly assessed damage occurring between 3 December 2017 and 23 February
    2018 in Eastern Ghouta Area, Syria (zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_Damascus_RDA_20180223_shp.zip
  format: null
  id: resource_9c1afe96
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Damascus_RDA_20180223_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_rapidlyassesseddamageoccu_20180301
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
  end: null
  start: '2018-03-01'
temporal_resolution: null
title: Rapidly assessed damage occurring between 3 December 2017 and 23 February 2018
  in Eastern Ghouta Area, Syria
version: null
vulnerability: null
---
