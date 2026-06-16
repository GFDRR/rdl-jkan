---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net/api/v2/users/1000
creator:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net/api/v2/users/1000
dataset_id: rdls_hzd-icpac_floodannualaveragenumberl
description: "Annual Average number of livestock units affected by floods in Projected\
  \ Climate Conditions.Future climate conditions for the years 2050-2100 are estimated\
  \ from the output of the EC\u2010EARTH3\u2010HR global model (Hazeleger et al.,\
  \ 2012) with RCP 8.5 and grid resolution of 0.5\xB0 (~55 km at the Equator). This\
  \ estimation is part of the results of a probabilistic regional flood risk assessment\
  \ developed for the Horn of Africa Partnership for Early Warning and Early Action\
  \ (developed by CIMA Foundation in cooperation with ICPAC, WFP, UNDRR, March 2021)\
  \ [Source: This metadata record was automatically extracted from the GeoNode portal\
  \ icpac]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: ICPAC
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/data0:geonode:admin1_livestock_projectedclimate
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:admin1_livestock_projectedclimate
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'FLOOD: Annual Average number of livestock units affected in Projected
    Climate Conditions (GHoA region) (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:admin1_livestock_projectedclimate&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:admin1_livestock_projectedclimate
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'FLOOD: Annual Average number of livestock units affected in Projected
    Climate Conditions (GHoA region) (OGC WFS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:admin1_livestock_projectedclimate&outputFormat=application%2Fjson
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-icpac_floodannualaveragenumberl
spatial:
  bbox:
  - 21.81368001500016
  - -11.74569511
  - 51.41551330000024
  - 23.142871801000183
  centroid: null
  countries:
  - AGO
  - BDI
  - BEN
  - BFA
  - BWA
  - CAF
  - CIV
  - CMR
  - COD
  - COG
  - COM
  - CPV
  - DJI
  - DZA
  - EGY
  - ERI
  - ETH
  - GAB
  - GHA
  - GIN
  - GMB
  - GNB
  - GNQ
  - KEN
  - LBR
  - LBY
  - LSO
  - MAR
  - MDG
  - MLI
  - MOZ
  - MRT
  - MUS
  - MWI
  - NAM
  - NER
  - NGA
  - RWA
  - SDN
  - SEN
  - SLE
  - SOM
  - SSD
  - STP
  - SWZ
  - SYC
  - TCD
  - TGO
  - TUN
  - TZA
  - UGA
  - ZAF
  - ZMB
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'FLOOD: Annual Average number of livestock units affected in Projected Climate
  Conditions (GHoA region)'
version: null
vulnerability: null
---
