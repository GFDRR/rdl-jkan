---
attributions:
- entity:
    affiliation: null
    email: null
    name: REACH initiative
    url: https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015
dataset_id: rdls_lss-syr_unosat_geodatadamagedensitycitie_20150721
description: 'This map illustrates satellite-detected areas of damage and destruction
  in the Syrian cities of Homs, Aleppo, Hama, Deir Ez Zor, Ar Raqqa, and Daraa. Using
  satellite imagery from 2015, 2014, 2013, 2011, and 2010, UNITAR - UNOSAT created
  a damage site density index for affected areas in each city. City-wide analyses
  revealed a total of 13,778 affected structures in Homs, 14,034 in Aleppo, 5,233
  in Hama, 3,416 in Deir Ez Zor, 1,601 in Ar Raqqa, and 966 in Daraa. The cities of
  Homs and Hama were not updated with 2015 imagery. This analysis was done of the
  REACH initiative for the U.S. Office of Foreign Disaster Assistance. This is a preliminary
  analysis & has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    from 2010-2015 across six Syrian cities, identifying notable changes and damage
    patterns between image pairs. A damage site density index was calculated for affected
    areas, resulting in structure-level damage counts per city (13,778 in Homs, 14,034
    in Aleppo, 5,233 in Hama, 3,416 in Deir Ez Zor, 1,601 in Ar Raqqa, 966 in Daraa).
    The dataset was produced for the REACH initiative and U.S. Office of Foreign Disaster
    Assistance to support humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: REACH initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction detected
      via satellite imagery
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
  description: Geodata of Damage Density in the Cities of Homs, Aleppo, Hama, Deir
    Ez Zor, Ar Raqqa, and Daraa, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
  format: null
  id: resource_164c5d23
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Density in the Cities of Homs, Aleppo, Hama, Deir
    Ez Zor, Ar Raqqa, and Daraa, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
  format: null
  id: resource_f61b76a6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_geodatadamagedensitycitie_20150721
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
  start: '2015-07-21'
temporal_resolution: null
title: Geodata of Damage Density in the Cities of Homs, Aleppo, Hama, Deir Ez Zor,
  Ar Raqqa, and Daraa, Syria
version: null
vulnerability: null
---
