---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-the-southeastern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-a
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-southeastern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-a
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-southeastern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-a
dataset_id: rdls_hl-pak_unosat_damageassessmentsoutheast_20191008
description: 'UNOSAT code: EQ20190924PAK This map illustrates satellite based structure
  damage assessment in the Southeastern part of New Mirpur City, Azad Kashmir, Pakistan
  that was affected by the 5.6 magnitude Mirpur earthquake of the 24th of September
  2019 with an epicenter SE of New Mipur City. UNITAR-UNOSAT has identified within
  the extent of this map 121 potentially damaged structures South of New Mirpur City.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-southeastern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-a]'
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
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired before
    and after the 24 September 2019 Mirpur earthquake to identify notable structural
    changes. Damage assessment was conducted through visual interpretation of satellite
    imagery, identifying 121 potentially damaged structures in the Southeastern part
    of New Mirpur City. This preliminary analysis was not field-validated at the time
    of publication.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-the-southeastern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-a
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-based assessment of 121 potentially damaged structures
      in Southeastern New Mirpur from the 5.6 magnitude earthquake
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage assessment in the Southeastern part of New Mirpur, Azad Jammu
    and Kashmir, Pakistan, as of 02 October 2019 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_gdb.zip
  format: Geodatabase
  id: resource_c7adb184
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
  description: Damage assessment in the Southeastern part of New Mirpur, Azad Jammu
    and Kashmir, Pakistan, as of 02 October 2019 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_SHP.zip
  format: null
  id: resource_8365f429
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20190924PAK_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-pak_unosat_damageassessmentsoutheast_20191008
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
  start: '2019-10-08'
temporal_resolution: null
title: Damage assessment in the Southeastern part of New Mirpur, Azad Jammu and Kashmir,
  Pakistan, as of 02 October 2019
version: null
vulnerability: null
---
