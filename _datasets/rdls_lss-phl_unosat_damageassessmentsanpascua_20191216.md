---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-san-pascual-municipality-northeastern-part-of-the-masbate-region-bico
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-san-pascual-municipality-northeastern-part-of-the-masbate-region-bico
dataset_id: rdls_lss-phl_unosat_damageassessmentsanpascua_20191216
description: 'UNOSAT code: TC20191202PHL This map illustrates satellite-based structural
  damage assessment in San Pascual municipality in the northeastern part of Masbate
  region, Bicol Region province, in the Philippines. The area was affected by Typhoon
  Kammuri that made landfall on 3 December 2019. UNITAR-UNOSAT identified 16 potentially
  damaged structures around San Pascual town, in the San Pascual municipality, within
  the extent of this map. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-of-san-pascual-municipality-northeastern-part-of-the-masbate-region-bico]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    acquired before and after Typhoon Kammuri's landfall on 3 December 2019 to identify
    structural changes and damage signatures. Potentially damaged structures (n=16)
    were manually delineated and mapped as point or polygon features with damage indicators
    and metadata in geodatabase and shapefile formats.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-san-pascual-municipality-northeastern-part-of-the-masbate-region-bico
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct structural damage to buildings from Typhoon Kammuri assessed
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Philippines - Damage Assessment of San Pascual Municipality, Northeastern
    Part of the Masbate Region, Bicol Region Province (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/TC20191202PHL/TC20191202PHL_gdb.zip
  format: Geodatabase
  id: resource_05edb575
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20191202PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Damage Assessment of San Pascual Municipality, Northeastern
    Part of the Masbate Region, Bicol Region Province (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/TC20191202PHL/TC20191202PHL_SHP.zip
  format: null
  id: resource_b3cc73d2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20191202PHL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_unosat_damageassessmentsanpascua_20191216
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-12-16'
temporal_resolution: null
title: Philippines - Damage Assessment of San Pascual Municipality, Northeastern Part
  of the Masbate Region, Bicol Region Province
version: null
vulnerability: null
---
