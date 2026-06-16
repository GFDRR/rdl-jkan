---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of-02-october-2019
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of-02-october-2019
dataset_id: rdls_lss-pak_unosat_damageassessmentnewmirpur_20191004
description: 'UNOSAT code: EQ20190924PAK This map illustrates satellite based building
  damage assessment in New Mirpur City, Azad Kashmir, Pakistan affected by the 5.6
  magnitude Mirpur earthquake of the 24th of September 2019 with an epicenter SE of
  New Mipur City. UNITAR-UNOSAT identified within the extent of this map 39 potentially
  damaged structures in New Mirpur City and surroundings. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  -UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of-02-october-2019]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired before
    and after the 24 September 2019 Mirpur earthquake to identify notable changes
    in building structures. Visual interpretation of satellite data identified 39
    potentially damaged structures in New Mirpur City and surroundings. This is a
    preliminary satellite-based damage assessment not yet validated through field
    surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of-02-october-2019
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 5.6 magnitude Mirpur earthquake
      of 24 September 2019
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
  description: Damage assessment in New Mirpur, Azad Jammu and Kashmir, Pakistan,
    as of 02 October 2019 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_gdb.zip
  format: Geodatabase
  id: resource_f99a31bf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20190924PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in New Mirpur, Azad Jammu and Kashmir, Pakistan,
    as of 02 October 2019 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_SHP.zip
  format: null
  id: resource_d976f0da
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20190924PAK_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pak_unosat_damageassessmentnewmirpur_20191004
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
  start: '2019-10-04'
temporal_resolution: null
title: Damage assessment in New Mirpur, Azad Jammu and Kashmir, Pakistan, as of 02
  October 2019
version: null
vulnerability: null
---
