---
attributions:
- entity:
    affiliation: null
    email: jrc-risk-data-hub@ec.europa.eu
    name: European Commision (EC), Joint Research Centre (JRC)
    url: https://joint-research-centre.ec.europa.eu/
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: estat-gisco@ec.europa.eu
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
creator:
  affiliation: null
  email: estat-gisco@ec.europa.eu
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
dataset_id: rdls_exp-jrc_drmkc_giscoport
description: Global dataset of ports
details: "The dataset contains a pointfeature class with the location of 2440 pan-European\
  \ ports, plus one attribute table and 3 domain tables. The ports are identified\
  \ following the UN Locode list. The dataset is based on the list \u201CPorts Estat\
  \ 2010\u201D from Eurostat. All ports are represented by a point location in PORT_PT_2013.\
  \ Point coordinates and Locodes are derived from several input sources, including\
  \ ports lists from EMSA, Lloyds, Norie\u2019s Seaports of the World, the GISCO Ports\
  \ 2010 dataset and the UN/LOCODE 2007 list. Attributes in PORT_AT_2013 include the\
  \ port name, Locode Status Indicator, and reliability flags for the positional and\
  \ Locode accuracy. Dataset coverage is global. The dataset has been created for\
  \ cartographic purposes and for appropriate analysis. Port statistics can be geo-referenced\
  \ to this high quality pan-European dataset, especially when based on UN Locode."
exposure:
- asset_type: null
  category: infrastructure
  id: exp_1
  metrics:
  - dimension: structure
    id: port
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Commission, Eurostat/GISCO
    risk_data_type: null
    type: dataset
    url: https://ec.europa.eu/eurostat/web/gisco
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
publisher:
  affiliation: null
  email: null
  name: European Commission, Eurostat/GISCO
  url: https://ec.europa.eu/eurostat/web/gisco
purpose: To provide a comprehensive global dataset of port locations with standardized
  UN Locode identifiers for cartographic applications, spatial analysis, and geo-referencing
  of port statistics.
referenced_by: []
resources:
- access_url: https://ec.europa.eu/eurostat/web/gisco/geodata/transport-networks
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4258
  description: The dataset contains a pointfeature class with the location of 2440
    pan-European ports, plus one attribute table and 3 domain tables.
  download_url: https://ec.europa.eu/eurostat/cache/GISCO/geodatafiles/PORT_2013_SH.zip
  format: null
  id: gisco_port_2013
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global dataset of ports
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_giscoport
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
title: GISCO Global Ports 2013
version: '2013'
vulnerability: null
---
