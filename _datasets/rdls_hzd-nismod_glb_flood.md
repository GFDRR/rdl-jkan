---
contact_point:
  email: samantha.kuzma@wri.org
  id: attribution_contact
  name: Samantha Kuzma
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
creator:
  email: samantha.kuzma@wri.org
  id: attribution_creator
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
dataset_id: rdls_hzd-nismod_glb_flood
description: Gridded flood inundation hazard maps showing riverine and coastal flood
  risks globally, with inundation depth measurements in meters for multiple return
  periods (2-year to 1000-year floods) under current baseline conditions and future
  climate projections for 2030, 2050, and 2080.
details: The dataset uses hydrological data from 1960-1999 for current flood scenarios
  and incorporates five Global Climate Models (GCMs) from CMIP5 under two climate
  scenarios (RCP4.5 and RCP8.5) and socio-economic pathways (SSP2 and SSP3) from the
  IPCC Fifth Assessment Report for future projections. The dataset is recommended
  for large-scale regional analysis, preliminary assessments, and evaluating relative
  changes in flood impacts under different climate scenarios. It is not suitable for
  detailed property-specific flood inundation mapping, analyzing flat lowland rivers
  with significant backwater effects, or assessing the impact of hydraulic structures.
  Flood hazard maps represent situations with no flood protection measures and may
  overestimate flood extent where protection infrastructure exists.
exposure: []
extra_attributions:
- email: dccinfo@rws.nl
  id: attribution_funder
  name: Dutch Ministry of Infrastructure and Water Management
  role: funder
  url: https://www.rijkswaterstaat.nl/en
- email: info@vu.nl
  id: attribution_collaborator_1
  name: Vrije Universiteit Amsterdam Institute for Environmental Studies
  role: collaborator
  url: https://vu.nl/en/about-vu/research-institutes/ivm
- email: info@deltares.nl
  id: attribution_collaborator_2
  name: Deltares
  role: collaborator
  url: https://www.deltares.nl/en
- email: info@uu.nl
  id: attribution_collaborator_3
  name: Utrecht University
  role: collaborator
  url: https://www.uu.nl/en
- email: info@pbl.nl
  id: attribution_collaborator_4
  name: PBL Netherlands Environmental Assessment Agency
  role: collaborator
  url: https://www.pbl.nl/en
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: coastal_flood, flood
  intensity: wd:m
  occurrence_range: Return periods from 2, 5, 10, 25, 50, 100, 250, 500, and 1000
    years
  processes: coastal_flood, fluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: Aqueduct
  url: https://www.wri.org/aqueduct
publisher:
  email: samantha.kuzma@wri.org
  id: attribution_publisher
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
purpose: The dataset was created to measure and map water-related flood risks worldwide
  to help decision-makers protect communities, target investments, and mitigate future
  flood risks. It enables users to conduct comprehensive cost-benefit analysis to
  evaluate the value of flood protection strategies, including dike protection measures.
resources:
- coordinate_system: EPSG:4326
  description: Global flood inundation depth maps for coastal and riverine hazards
    derived from the WRI Aqueduct Flood Tool. This collection encompasses historical
    baseline conditions and future climate projections (RCP4.5 and RCP8.5) for the
    years 2030, 2050, and 2080. It includes scenarios with and without land subsidence
    across multiple return periods (2, 5, 10, 25, 50, 100, 250, 500, and 1000 years).
    The riverine models utilize various GCMs including NorESM1-M, GFDL-ESM2M, HadGEM2-ES,
    IPSL-CM5A-LR, and MIROC-ESM-CHEM.
  download_url: https://wri-projects.s3.amazonaws.com/AqueductFloodTool/download/v2/index.html
  format: GeoTIFF (tif)
  id: wri_aqueduct_flood_inundation_depth_collection
  media_type: null
  spatial_resolution: 1000
  temporal:
    duration: P70Y
    end: '2080'
    start: '2010'
    temporal_resolution: ''
  title: WRI Aqueduct Coastal and Riverine Flood Inundation Depth (Historical and
    Future Projections)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-nismod_glb_flood
spatial:
  countries:
  - GLO
  scale: global
title: Aqueduct Floods Hazard
version: '2'
vulnerability: null
---
