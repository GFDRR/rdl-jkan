---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: ivan.luque.segura@rmit.edu.au
  name: Ivan Luque
  url: https://maps.eurac.edu/api/v2/users/1006
creator:
  affiliation: null
  email: andrea.vianello@eurac.edu
  name: Andrea Vianello
  url: https://maps.eurac.edu/api/v2/users/1000
dataset_id: rdls_exp-eurac_occupantbehaviourmodellin
description: 'This layer aims at creating a knowledge base related to research on
  Occupant Behaviour Modelling. The main Cultural-E contribution referrers to the
  translation into a GIS format of the provision of open-access available review tables
  focused on occupants'' perception and behaviour in buildings (OPA)(*). In contrast
  to tables often found in supplementary materials, which are static, the tables used
  are dynamically growing with new evidence appearing in scientific literature. Authors
  of original research are welcome to add their published and peer-reviewed research
  items to these tables. (*) Schweiker M, Andersen RK, Berger C, Carlucci S, Chinazzo
  G, Edappilly LP, Favero M, Mahdavi A, Piselli C, Bourikas L, Hong T, Dong B, Syndicus
  M and Hahn J (2021) Dynamic review tables for topical reviews on occupants'' perception
  and behaviour in buildings. OSF. Available at: osf.io/gnvp2 [Source: This metadata
  record was automatically extracted from the GeoNode portal eurac]'
details: 'The filtering feature of this layer allows to identify specific aspects
  from the knowledge base related to research on Occupant Behaviour Modelling table
  (*). Such as the following attributes: - Occupant presence or actions: 1. Appliance
  use 2. Clothing adjustment 3. Lighting operation 4. Presence 5. Shading operation
  6. Thermostat adjustment 7. Window operation - Building use: 1. Office building
  2. Office building (university) 3. Residential building 4. Educational building
  5. Commercial building 6. Hotel 7. District 8. General purpose 9. Outdoors In addition,
  the entries referred to the following type of building, which could be filtered
  as part of the referred table (*): 1. Natural ventilation 2. Mechanical ventilation
  2. Mechanical heating + Natural ventilation 3. Mechanical heating and cooling 4.
  Mechanical cooling 5. Mechanical heating and cooling and natural ventilation'
exposure:
- asset_type: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-nc/4.0/
lineage:
  description: 'Data source: Schweiker M, Andersen RK, Berger C, Carlucci S, Chinazzo
    G, Edappilly LP, Favero M, Mahdavi A, Piselli C, Bourikas L, Hong T, Dong B, Syndicus
    M and Hahn J (2021) Dynamic review tables for topical reviews on occupants'' perception
    and behaviour in buildings. OSF. Available at: osf.io/gnvp2'
  sources:
  - id: source_1
    license: null
    name: Andrea Vianello
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/994
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Andrea Vianello
  url: https://maps.eurac.edu
purpose: 'The main Cultural-E contribution referrers to the translation into a GIS
  format of the provision of open-access available review tables focused on occupants''
  perception and behaviour in buildings (OPA)(*). (*)Data source: Schweiker M, Andersen
  RK, Berger C, Carlucci S, Chinazzo G, Edappilly LP, Favero M, Mahdavi A, Piselli
  C, Bourikas L, Hong T, Dong B, Syndicus M and Hahn J (2021) Dynamic review tables
  for topical reviews on occupants'' perception and behaviour in buildings. OSF: osf.io/gnvp2'
referenced_by:
- author_names: null
  date_published: null
  doi: osf.io/gnvp2
  id: ref_doi
  name: null
  url: https://doi.org/sf.io/gnvp2
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (GML 2.0)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_0
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (CSV)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (Zipped Shapefile)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (GML 3.1.1)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (Excel)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Occupant Behaviour Modelling (JSON)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AOBM_v02&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:OBM_v02
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Occupant Behaviour Modelling (OGC WMS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:OBM_v02&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:OBM_v02
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Occupant Behaviour Modelling (OGC WFS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:OBM_v02&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eurac_occupantbehaviourmodellin
spatial:
  bbox:
  - -31.6483516693115
  - 27.4207515716553
  - 45.200813293457
  - 71.4018936157227
  centroid: null
  countries:
  - ALB
  - AND
  - AUT
  - BEL
  - BGR
  - BIH
  - BLR
  - CHE
  - CYP
  - CZE
  - DEU
  - DNK
  - ESP
  - EST
  - FIN
  - FRA
  - GBR
  - GRC
  - HRV
  - HUN
  - IRL
  - ISL
  - ITA
  - LIE
  - LTU
  - LUX
  - LVA
  - MCO
  - MDA
  - MKD
  - MLT
  - MNE
  - NLD
  - NOR
  - POL
  - PRT
  - ROU
  - RUS
  - SMR
  - SRB
  - SVK
  - SVN
  - SWE
  - UKR
  - VAT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: 2022
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Occupant Behaviour Modelling
version: null
vulnerability: null
---
