---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-and-displaced-persons-visible-in-satellite-imagery-kathmand-april-28-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-and-displaced-persons-visible-in-satellite-imagery-kathmand-april-28-2015
dataset_id: rdls_lss-npl_unosat_geodatadamagedisplacedper_20150428
description: 'UNITAR/UNOSAT analyzed satellite imagery collected 27 April 2015 by
  the Pleiades satellite over the city of Kathmandu, Nepal. Damaged structures and
  the locations of displaced persons were identified. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR/UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-and-displaced-persons-visible-in-satellite-imagery-kathmand-april-28-2015]'
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 27
    April 2015 over Kathmandu, comparing pre- and post-earthquake images to identify
    notable changes. Damaged building structures and locations of displaced persons
    were manually delineated and georeferenced as point and polygon features in KMZ
    format. This preliminary analysis was not field-validated.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-and-displaced-persons-visible-in-satellite-imagery-kathmand-april-28-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake identified through satellite
      imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: Displaced persons identified through satellite imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Geodata of Damage and Displaced Persons Visible in Satellite Imagery.
    Kathmandu, Nepal - 27 April 2015 (KML)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/Kathmandu_Nepal_27April2015_IDP_Damage.kmz
  format: null
  id: resource_7f39e33f
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kathmandu_Nepal_27April2015_IDP_Damage.kmz
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_unosat_geodatadamagedisplacedper_20150428
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-28'
temporal_resolution: null
title: Geodata of Damage and Displaced Persons Visible in Satellite Imagery. Kathmandu,
  Nepal - 27 April 2015
version: null
vulnerability: null
---
