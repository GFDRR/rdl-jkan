---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014
dataset_id: rdls_lss-ssd_unosat_geodatadamageassesmentcit_20140321
description: 'This map illustrates satellite-detected areas of destruction in the
  town of Malakal as seen by the WorldView-1 satellite on 15 March 2014. UNOSAT identified
  a total of 9,878 destroyed residential and related structures and a total of 204
  destroyed warehouse or commercial structures throughout the area analyzed. Comparison
  with pre-conflict building data for Malakal indicates the 22% of the city has been
  destroyed. The previous UNOSAT analysis of Malakal using an image from 18 January
  2014 located 573 destroyed structures, meaning a massive increase in the level of
  damage is present as of 15 March 2014. The heaviest damage is found in the eastern
  and southern portions though is also present across the city. As of 15 March, active
  fires were visible in Malakal (see inset), as are fortifications and indications
  of military activity. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014]'
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
  description: UNOSAT analysts compared WorldView-1 satellite imagery from 15 March
    2014 with pre-conflict baseline building data for Malakal to identify and count
    destroyed structures. Multi-temporal satellite image comparison detected notable
    changes in building presence, classifying 9,878 destroyed residential structures
    and 204 destroyed commercial structures, representing 22% of the city's building
    stock.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Malakal
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
  description: Geodata of Damage Assesment In The City Of Malakal, Upper Nile State,
    South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_abc22fac
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assesment In The City Of Malakal, Upper Nile State,
    South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_ab576fcb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_unosat_geodatadamageassesmentcit_20140321
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-03-21'
temporal_resolution: null
title: Geodata of Damage Assesment In The City Of Malakal, Upper Nile State, South
  Sudan
version: null
vulnerability: null
---
