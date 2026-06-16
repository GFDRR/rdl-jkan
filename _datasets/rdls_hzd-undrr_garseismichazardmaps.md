---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for Disaster Risk Reduction (UNDRR)
    url: http://www.undrr.org
  id: attribution_publisher_1765296204845
  role: publisher
- entity:
    affiliation: null
    email: null
    name: International Centre for Numerical Methods in Engineering (CIMNE)
    url: https://cimne.com/
  id: attribution_creator_1765296231939
  role: creator
- entity:
    affiliation: null
    email: null
    name: GAR Risk Data Platform
    url: https://risk.preventionweb.net/
  id: attribution_contact_point_1765297532214
  role: contact_point
catalog: GAR PreventionWeb
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: http://www.undrr.org
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: http://www.undrr.org
dataset_id: rdls_hzd-undrr_garseismichazardmaps
description: For the GAR Atlas, a fully probabilistic seismic hazard analysis at global
  level was developed by CIMNE and INGENIAR Ltda. This hazard model is a continuation
  and improvement of the one developed in the framework of GAR13 where a set of tectonic
  provinces were identified and characterized by means of a set of parameters that
  describe the future seismic activity on each of them based on historical records
  together with relationships to obtain hazard intensities as a function of magnitude
  and distance. The hazard analysis was performed using the program CRISIS2014, a
  state-of-the-art tool for these kinds of tasks and widely known and acknowledged
  by experts in the field across the world. The chosen hazard intensity measure for
  this case was spectral acceleration and to guarantee a good connection between the
  hazard and the exposure characteristics, results for several ordinates beteween
  0.0 and 2.3 seconds were computed.
details: This dataset was developed in the framework of an analysis with a global
  scope and should not be used for local applications and/or decision-making purposes
  (such as land use planning). The main purpose of all GAR Atlas datasets is to broadly
  identify high risk areas at global level and also identifying areas where more detailed
  data should be collected and where detailed risk assessments are to be performed.
  Results for some areas may be underestimated or overestimated. UNISDR and its scientific
  partners and collaborators should in no case be liable for misuse or misinterpretation
  of the presented results. The designations employed and the presentation of material
  on the maps do not imply the expression of any opinion whatsoever on the part of
  UNISDR or the Secretariat of the United Nations concerning the legal status of any
  country, territory, city or area or of its authorities, or concerning the delimitation
  of its frontiers or boundaries.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: poisson
    hazards:
    - classification: null
      id: hazard_YiqnwZuB
      intensity_measure: AvgSa:cm/s2
      process: ground_motion
      trigger: null
      type: earthquake
    - classification: null
      id: hazard_5xnQJjDo
      intensity_measure: PGA:cm/s2
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_xjZnwJUB
    occurrence_range: RP 250, 475, 975, 1500, 2475 years
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GAR Atlas
  url: https://www.preventionweb.net/english/hyogo/gar/atlas/
publisher:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: http://www.undrr.org
purpose: null
referenced_by:
- author_names: null
  date_published: '2015-02-01'
  doi: null
  id: reference_YxN8cGq3
  name: 'Update on the probabilistic modelling of natural risks at global level: global
    risk model'
  url: https://www.preventionweb.net/english/hyogo/gar/2015/en/bgdocs/CIMNE_INGENIAR%20Background%20Paper%20Global%20Risk%20Model%20GAR%2015%20v1.3.pdf
resources:
- access_url: https://risk.preventionweb.net/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'The dataset download page includes: - Peak Ground Acceleration (PGA)
    - Spectral acceleration 0.2/0.5/1 sec Each are provided for return period scenarios
    250, 475, 975, 1500, 2475 years.'
  download_url: null
  format: GRID
  id: resource_UdLfzVrE
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 8000
  temporal: null
  temporal_resolution: null
  title: Peak ground acceleration and Spectral acceleration
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_garseismichazardmaps
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: GAR Seismic Hazard maps
version: '1.0'
vulnerability: null
---
